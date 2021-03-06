# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

# handle upload for cherrypy
#
#   this is done pretty ad hoc
#   the blueimp file upload js lib is used
#   the upload progress is done by server writing done the progress info
#   in a little file, and then on the client side every second
#   a request will be sent to update how much have been uploaded


import cherrypy

from .UploadConfiguration import UploadConfiguration

class Mixin:
    
    @cherrypy.expose
    @cherrypy.tools.json_out(content_type="text/html")
    def _luban_upload(self, uploadid=None, luban_upload_file=None, **kwds):
        
        # cherrypy.log('upload started id: %s, kwds:%s' % (uploadid, kwds) )
        cherrypy.response.timeout = UploadConfiguration.timeout
        
        if not isinstance(luban_upload_file, list):
            luban_upload_files = [luban_upload_file]
        else:
            luban_upload_files = luban_upload_file
            
        for luban_upload_file in luban_upload_files:
            # where to save the file
            fpath = _getUploadFilePath(luban_upload_file.filename, uploadid)
        
            # open output stream
            ostream = open(fpath, 'wb')
        
            # read uploaded data 
            data = luban_upload_file.file.read()
            size = len(data)

            # write it out
            ostream.write(data)
            ostream.close()
        
        return [
            {
                "name": luban_upload_file.filename,
                "size": size,
                "type": str(luban_upload_file.content_type),
            }
            for luban_upload_file in luban_upload_files
            ]


    @cherrypy.expose
    @cherrypy.tools.json_out(content_type="text/html")
    def _luban_upload_progress(self, id, **kwds):
        f = _getUploadProgressFilePath(id)
        import  os
        if not os.path.exists(f):
            value = None
        else:
            value = open(f).read()
            # see below in part_read_lines_to_boundary
            # how this file is written
            value = eval(value)
        return value


    @classmethod
    def _getUploadFilePath(cls, filename, id):
        return _getUploadFilePath(filename, id)


def _getUploadFilePath(filename, id):
    import os
    dir = _getUploadFileContainerDir(id)
    return os.path.join(dir, filename)


def _getUploadRoot():
    import os
    dir = UploadConfiguration.path
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir


def _getUploadFileContainerDir(id):
    import os
    dir = os.path.join(_getUploadRoot(), id)
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir


def _getUploadProgressFilePath(id):
    dir = _getUploadRoot()
    import os
    return os.path.join(dir, '%s-progress' % id,)


# overload cherrpy default behavior so we can handle upload
# more efficiently
# the implementation here is really not good.
# there should be a better way to do this to overload the cherrypy
# behavior.
from cherrypy._cpreqbody import Entity, SizedReader, ntob, Part
saved_entity_process = Entity.process
def overload_entity_process(self):
    """Execute the best-match processor for the given media type."""
    name = self.name
    if not name:
        return saved_entity_process(self)
    sig = 'luban_upload_file: '
    if self.name.startswith(sig):
        cherrypy.request.uploadid = self.uploadid = self.name[len(sig):]
        self.name = 'luban_upload_file'
        return process_upload_file(self)
    return saved_entity_process(self)
Entity.process = overload_entity_process

def process_upload_file(self):
    # cherrypy.log("enter process_upload_file")
    if self.length and self.length > UploadConfiguration.limit:
        raise cherrypy.HTTPError(413, "file size too large")
        
    saved_entity_process(self)
    return


def part_read_lines_to_boundary(self, fp_out=None):
    """Read bytes from self.fp and return or write them to a file.

    If the 'fp_out' argument is None (the default), all bytes read are
    returned in a single byte string.

    If the 'fp_out' argument is not None, it must be a file-like object that
    supports the 'write' method; all bytes read will be written to the fp,
    and that fp is returned.
    """
    # ---  added code -----------------------
    try:
        uploadid = cherrypy.request.uploadid
    except:
        uploadid = None
    read = 0
    # ----------------------------------------
    
    endmarker = self.boundary + ntob("--")
    delim = ntob("")
    prev_lf = True
    lines = []
    seen = 0
    while True:
        line = self.fp.readline(1<<16)

        # ---  added code -----------------------
        read += len(line)
        if read > UploadConfiguration.limit:
            raise cherrypy.HTTPError(413)
        
        if uploadid:
            progress_file = _getUploadProgressFilePath(uploadid)
            pfs = open(progress_file, 'w')
            data = {'increment': len(line), 'uploaded': read}
            pfs.write(str(data))
            pfs.flush()
            pfs.close()
        # ----------------------------------------

        if not line:
            raise EOFError("Illegal end of multipart body.")
        if line.startswith(ntob("--")) and prev_lf:
            strippedline = line.strip()
            if strippedline == self.boundary:
                break
            if strippedline == endmarker:
                self.fp.finish()
                break

        line = delim + line

        if line.endswith(ntob("\r\n")):
            delim = ntob("\r\n")
            line = line[:-2]
            prev_lf = True
        elif line.endswith(ntob("\n")):
            delim = ntob("\n")
            line = line[:-1]
            prev_lf = True
        else:
            delim = ntob("")
            prev_lf = False

        if fp_out is None:
            lines.append(line)
            seen += len(line)
            if seen > self.maxrambytes:
                fp_out = self.make_file()
                for line in lines:
                    fp_out.write(line)
        else:
            fp_out.write(line)

    if fp_out is None:
        result = ntob('').join(lines)
        for charset in self.attempt_charsets:
            try:
                result = result.decode(charset)
            except UnicodeDecodeError:
                pass
            else:
                self.charset = charset
                return result
        else:
            raise cherrypy.HTTPError(
                400, "The request entity could not be decoded. The following "
                "charsets were attempted: %s" % repr(self.attempt_charsets))
    else:
        fp_out.seek(0)
        return fp_out
Part.read_lines_to_boundary = part_read_lines_to_boundary


# End of file 

