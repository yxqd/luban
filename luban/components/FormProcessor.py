# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



from pyre.components.Component import Component

class FormProcessorInterface(Component):


    class Inventory(Component.Inventory):

        import luban.inventory
        formid = luban.inventory.str(name='formid')

        # post processing parameters
        #  old_display_id: id of the old display to be replaced0
        old_display_id = luban.inventory.str(name='old_display_id')
        #  new_display_creator: routine to create new visual
        new_display_creator = luban.inventory.str(name='new_display_creator')
        

    def process(self, director):
        errors = self._getInputErrors()
        if errors:
            return self._reportErrors(errors)
        return self._postProcessing(director)


    def _castInventoryProperties(self):
        """luban inventor items are not casted immediately. this is the place
        where casting happens. This method is not necessary for actors that store
        user inputs to db, because the db column descriptors will do the casting.
        """
        from luban.inventory.properties.PropertyInterface import PropertyInterface
        from luban.inventory.properties.PropertySet import PropertySet
        for name in dir(self.Inventory):
            trait = getattr(self.Inventory, name)
            if not isinstance(trait, PropertyInterface): continue
            if isinstance(trait, PropertySet):
                # use inventory.<name>.getValues() to get casted values
                continue
            value = getattr(self.inventory, name)
            value = trait.convertValue(value)
            setattr(self.inventory, name, value)
            continue
        return


    def _postProcessing(self, director):
        self.store(director)
        return self._postStoringUserInputs(director)


    def _postStoringUserInputs(self, director):
        old_display_id = self.inventory.old_display_id
        if not old_display_id: old_display_id = self.inventory.formid

        new_display_creator = self.inventory.new_display_creator
        if not new_display_creator: new_display_creator = 'display'
        new_display = getattr(self, new_display_creator)(director)

        from luban.content import select
        return select(id=old_display_id).replaceBy(new_display)


    def _reportErrors(self, errors):
        from luban.content import select
        form = select(id=self.inventory.formid)
        actions = [
            form.find(name=name).formfield('showError', message=error)
            for name, error in errors.iteritems()
            ]
        return actions


    def _getInputErrors(self):
        errors = {}
        from luban.inventory.properties.PropertyInterface import PropertyInterface
        from luban.inventory.properties.PropertySet import PropertySet
        for name in dir(self.Inventory):
            trait = getattr(self.Inventory, name)
            if not isinstance(trait, PropertyInterface): continue
            if isinstance(trait, PropertySet):
                pset = getattr(self.inventory, name)
                errors.update(pset.getValueErrors())
                continue
            value = getattr(self.inventory, name)
            e = trait.getValueError(value)
            if e:
                errors[name] = e
            continue
        return errors


    # the actor can now accept arbitrary inputs
    def updateConfiguration(self, registry):
        listing = self._listing(registry)
        if listing:
            for k, v in listing:
                setattr(self.inventory, k, v)        
        return []

    
    def _listing(self, registry):
        if not registry: return []
        listing = [
            (name, descriptor.value) for name, descriptor in registry.properties.iteritems()
            ]

        listing += [
            ("%s.%s" % (nodename, name), value)
            for nodename, node in registry.facilities.iteritems()
            for name, value in self._listing(node)
            ]

        return listing


from AuthorizedActor import AuthorizedActor
class FormProcessor(FormProcessorInterface, AuthorizedActor):
    class Inventory(FormProcessorInterface.Inventory, AuthorizedActor.Inventory):
        pass


# version
__id__ = "$Id$"

# End of file 
