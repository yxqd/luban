#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                             Michael A.G. Aivazis
#                      California Institute of Technology
#                      (C) 1998-2005  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#
# Modified from opal.applications.CGI --Jiao Lin
#


class CGIInputCollector:


    stdin_size_limit = 1024*1024*16
    debug = True
    log = '../log/CGIInputCollector.log'


    def __init__(self):
        self._uploads = None
        if self.debug:
            log = os.path.abspath(self.log)
            self._debug_out = open(log, 'w')
        return


    def __call__(self, *args, **kwds):
        try:
            self.collectCGIInput(*args, **kwds)
        except:
            import traceback
            self._log(traceback.format_exc())
            raise
        self._log('cgi input processed')
        

    def getCGIInput(self):
        return self._cgi_input
    

    def getUploads(self):
        return self._uploads

    
    def collectCGIInput(self, registry, argv):
        parser = self.parser
        
        # get access to the environment variables
        import os

        # remember the cgi input so that we can output them when necessary (debug)
        self._cgi_input = os.environ.copy()

        #
        if os.environ.has_key('REQUEST_PICKLED'):
            self._collectCGIInputFromPickledRequest(registry)
        else:
            self._collectCGIInput(registry)
                                                           
        # if we got commandline arguments, parse them as well
        for arg in argv:
            if arg and arg[0] == '?':
                arg = arg[1:]
            parser.parse(registry, arg, 'command line')
        return


    def _collectCGIInputFromPickledRequest(self, registry):
        # this method collect cgi input from the request object generated
        # by the "SimpleHTTPServer"
        parser = self.parser
        
        import pickle
        request = pickle.loads(os.environ['REQUEST_PICKLED'])
        del os.environ['REQUEST_PICKLED']
        cookie = pickle.loads(os.environ['COOKIE_PICKLED'])
        del os.environ['COOKIE_PICKLED']

        # cookie
        for k, v in cookie.iteritems():
            self._log('%s\t%s' % (k,v.value))
            parser._processArgument(k,v.value, registry)
            continue
        
        for k, v in request.iteritems():

            # see SimpleHTTPServer
            v = ','.join(v)

            self._log('%s\t%s' % (k,v))
            
            parser._processArgument(k,v, registry)
            continue

        return
            

    def _collectCGIInput(self, registry):
        # create a parser for query strings
        parser = self.parser

        # figure out the request method
        try:
            method = os.environ['REQUEST_METHOD'].upper()
        except KeyError:
            method = 'GET'

        # extract the headers
        headers = {}
        headers['content-type'] = os.environ.get(
            'CONTENT_TYPE', 'application/x-www-form-urlencoded')
        try:
            headers['content-length'] = os.environ['CONTENT_LENGTH']
        except KeyError:
            pass


        # process arguments from cookie
        cookie = os.environ.get('HTTP_COOKIE')
        if cookie:
            self._parseCookieToQuery(cookie)
        
        # process arguments from query string
        if method == 'GET' or method == 'HEAD':
            try:
                query = os.environ['QUERY_STRING']
            except KeyError:
                pass
            else:
                parser.parse(registry, query, 'query string')
                
        elif method == 'POST':
            
            try:
                query = os.environ['QUERY_STRING']
            except KeyError:
                pass
            else:
                parser.parse(registry, query, 'query string')

            content_type = headers['content-type']
            
            normalform = 'application/x-www-form-urlencoded'
            if content_type[:len(normalform)] == normalform:
                import sys
                inlines = []
                for line in sys.stdin:
                    inlines.append(line)
                    parser.parse(registry, line, 'form')
                self._cgi_input['sys.stdin'] = inlines
                    
            elif content_type.find( 'multipart/form-data' ) != -1:
                self._handle_upload(headers, registry, parser)
                
            else:
                import journal
                firewall = journal.firewall('luban')
                firewall.log("NYI: unsupported content-type '%s'" % content_type)
        else:
            import journal
            journal.firewall('luban').log("unknown method '%s'" % method)

        return


    def _handle_upload(self, headers, registry, parser):
        # file upload handling

        # mime parser
        from email.FeedParser import FeedParser
        fp = FeedParser()

        # need header
        content_type = headers['content-type']
        fp.feed( 'CONTENT-TYPE: %s\n' % content_type )

        # size limit
        size_limit = self.stdin_size_limit

        # read in chunks
        chunk_size = 8192

        # number of chunks
        n = size_limit/chunk_size
        
        # feed contents from stdin to parser
        import sys
        i=0; succeeded = False
        while i<n:
            data = sys.stdin.read( chunk_size )
            if not data: succeeded = True; break
            fp.feed( data )
            continue
        if not succeeded:
            raise RuntimeError, "stdin too large"
        
        # parsed is a mime instance
        parsed = fp.close()

        #
        header = 'Content-Disposition'

        if self.debug: 
            self._cgi_input['uploaded mime'] = parsed.as_string()

        args = []
        uploads = {}
        for part in parsed.walk():

            if part.get_content_maintype() == 'multipart':
                # this part is the parent message it self, skip
                continue

            filename = part.get_param( 'filename', header = header )
            key = part.get_param( 'name', header = header )
            if filename:
                # this means we are dealing with a real file
                # save them to a dictionary so that later actors can handle them
                content = part.get_payload(decode=True)
                # uploads[filename] = content
                uploads[key] = filename, content
            else:
                # just a key,value pair
                value = part.get_payload()
                args.append( (key,value) )

            # pass key,value pairs to pyre option registry
            arg = '&'.join( [ '%s=%s' % (k,v) for k,v in args] )
            if arg: parser.parse( registry, arg, 'form' )

        self._uploads = uploads
        return

    
    def _parseCookieToQuery(self, cookie):
        # parse cookie to look like query string
        cookies = cookie.split(';')
        cookies = [cookie.strip() for cookie in cookies]
        cookie = '&'.join(cookies)

        # add it into the query string
        import os
        query = os.environ.get('QUERY_STRING')
        if not query:
            query = cookie
        else:
            query = cookie+'&'+query
        os.environ['QUERY_STRING'] = query

        self._cgi_input['QUERY_STRING_MODIFIED'] = query
        return
    

    def _createCGIParser(self):
        from CGIParser import CGIParser
        return CGIParser(strict=False, keepBlanks=False, log=self._log)


    def _getCGIParser(self):
        key = '_cgiparser'
        if not hasattr(self, key):
            setattr(self, key, self._createCGIParser())
        return getattr(self, key)
    parser = property(_getCGIParser)


    def _log(self, msg):
        if self.debug:
            print >> self._debug_out, msg
        return    
        

import os, sys

# version
__id__ = "$Id: CGI.py,v 1.6 2008-04-21 07:51:08 aivazis Exp $"

# End of file 
