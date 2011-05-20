

def retrieveConfiguration(inventory, registry):
    """place the current inventory configuration in the given registry"""
    
    from pyre.inventory.Facility import Facility
    from pyre.inventory.Property import Property
    from journal.components.Journal import Journal
    
    node = registry.getNode(inventory._priv_name)
    
    for prop in inventory.properties():
        
        name = prop.name
        descriptor = inventory.getTraitDescriptor(name)
        value = descriptor.value
        locator = descriptor.locator
        
        if name == "weaver": continue
        #if isinstance(prop, Property) and value == prop.default: continue
        if isinstance(prop, Facility) and isinstance(value, Journal): continue
        if isinstance(prop, Facility) and value: value = value.name
        
        node.setProperty(name, value, locator)
        continue
    
    for fac in inventory.facilities():
        component = fac.__get__(inventory)
        if isinstance(component, Journal): continue
        if component is None:
            # raise RuntimeError, "Unable to retrieve component for facility %s" % fac.name
            continue
        retrieveConfiguration(component.inventory, node)
        continue
    
    return registry



def toPml(pyreapp, path=None, stream=None):
    registry = pyreapp.createRegistry()
    registry = retrieveConfiguration( pyreapp.inventory, registry )
    weaver = pyreapp.inventory.weaver
    renderer = pyreapp.getCurator().codecs['pml'].renderer
    weaver.renderer = renderer
    if not stream:
        if not path: raise ValueError, 'neither path nor stream is supplied'
        stream = open(path, 'w')
    weaver.weave(registry, stream)
    return

                                                                                                                                                    
