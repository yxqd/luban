
section_markers = [
    '=',
    '-',
    '^',
    '\"',
    '\'',
    '*',
    ]
    

def widget_doc(widget_name, outmost_section_mark='\"'):
    widget = _imp_widget(widget_name)

    # this will be useful later if subsections is needed for a widget
    section_mark_index = section_markers.index(outmost_section_mark)
    
    lines = []

    # title
    name = widget.__name__
    if hasattr(widget, 'experimental') and widget.experimental:
        name += '(experimental)'
    title = ':mod:`%s`: %s' % (name, widget.simple_description)
    title_underline = outmost_section_mark*len(title)
    lines += [title, title_underline, '']
    
    lines.append(widget.full_description)
    lines.append('')

    # examples
    if hasattr(widget, 'examples') and widget.examples:
        examples = widget.examples
        for i, example in enumerate(examples):
            lines.append('Example %s::' % (i+1))
            lines.append('')
            lines += example.splitlines()
            lines.append('')
            continue
        lines.append('')
    #
    descriptors = widget.getDescriptors()
    descriptors = _categorizeDescriptors(descriptors)
    
    # props
    props = descriptors['properties']
    props = filter(lambda d: d.name in widget.__dict__, props)
    if props:
        lines.append('Properties:')
        lines.append('')
    for d in props:
        if hasattr(d, 'tip'): tip = d.tip
        else: tip = 'Please give a tip of property %s' % d.name

        # title
        title = '* ' + d.name
        if hasattr(d, 'experimental') and d.experimental:
            title += '(experimental)'
        title += ': ' + tip
        lines.append(title)
        lines.append(' ')

        # type
        lines.append('  * type: %s' % d.type)

        # validator
        validator = d.validator
        if validator:
            # choices
            if validator.__class__.__name__ == 'Choice':
                lines.append('  * allowed values: %s' % validator.value)

        lines.append('')
        continue
    lines.append('')
    
    # event handlers
    eventhandlers = descriptors['eventhandlers']
    eventhandlers = filter(lambda d: d.name in widget.__dict__, eventhandlers)
    if eventhandlers:
        lines.append('Event handlers:')
        lines.append('')
    for d in eventhandlers:
        if hasattr(d, 'tip'): tip = d.tip
        else: tip = 'Please give a tip of property %s' % d.name
            
        title = d.name
        if hasattr(d, 'experimental') and d.experimental:
            title += '(experimental)'
        title += ':' + tip
        lines.append('* ' + title)
        lines.append('')
        
        examplecode = widget.__name__.lower() + 'instance' + '.' + d.name + ' = some_action'
        lines.append('  * Example::')
        lines.append('    ')
        lines.append('      >>> ' + examplecode)
        continue
        
    #
    factories = _getElementFactoriesR(widget)
    if factories:
        lines.append('Factory methods for creating sub-elements:')
        lines.append('')
        for f in factories:
            name = f.__name__
            lines.append('* '+name)
            continue
    lines.append('')

    lines.append('Class information for %s:' % widget.__name__)
    lines.append('')
    lines.append('.. inheritance-diagram:: luban.content.%s' % widget.__name__)
    lines.append('   :parts: 1')
    lines.append('')
    lines.append('.. .. automodule:: luban.content.%s' % widget.__name__)
    lines.append('   :members:')
    lines.append('   :undoc-members:')
    return lines

"""
Factory methods for creating sub-elements

* document
"""
   

def _imp_widget(name):
    pkg = 'luban.content'
    tokens = name.split('.')
    modulename = '.'.join(tokens[:-1])
    klsname = tokens[-1]
    m = '%s.%s' % (pkg, modulename)
    m = __import__(m, {}, {}, [''])
    return getattr(m, klsname)


def _getElementFactoriesR(kls):
    ret = _getElementFactories1(kls)
    for base in kls.__bases__:
        ret += _getElementFactoriesR(base)
    return ret


def _getElementFactories1(kls):
    ret = []
    for k, v in kls.__dict__.iteritems():
        if hasattr(v, 'iselementfactory') and v.iselementfactory:
            ret.append(v)
    return ret


def _categorizeDescriptors(descriptors, skip=None):
    'put descriptors into different categories such as properties, eventhandlers'
    r = {
        'properties': [],
        'eventhandlers': [],
        }

    # contents is not really directly settable
    skip = skip or ['contents']

    from luban.content.descriptors import EventHandler
    for d in descriptors:
        if d.name in skip: continue
        if isinstance(d, EventHandler):
            r['eventhandlers'].append(d)
            continue
        r['properties'].append(d)
        continue

    return r
