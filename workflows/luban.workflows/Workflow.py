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



class Workflow:

    """
    base class of workflows

    a workflow is a container of components that are necessary
    for a workflow to work.

    first, a workflow is built upon a bunch of data object models.
    These models are to be manipulated in the workflow.
    For example, a login workflow at the least needs a "users" table
    or sth alike.
    Therefore, we require each workflow to provide a factory method
    to create models necessary for the workflow to function well.
    This factory method, however, must detect whether this required
    model already was defined (by looking up the model registry),
    and only define those models if it cannot find existing implementations.

    then, a workflow consists of an actor (**should we consider multiple
    actors? let us keep it simple for now**), and a visual factory that
    knows how to create visuals related to this workflow.

    Once created, a workflow class can be  customized and used by
    a luban app.

    See the implementation in .login for an example of a workflow.
    
    typical usage of a workflow
    1. create a customized workflow factory in a module
      from somewhere import Workflow
      @Workflow.factory
      def workflow(): return Workflow(...)

    2. in the actor module:
      from workflow_module import workflow
      class Actor(workflow().Actor): ...

    3. when creating a visual:
      from workflow_module import workflow
      form = workflow().visuals.form(...)
    """

    # factory of models. this should probably not really be used
    # by real applications.
    # it just gathers all the models necessary for this workflow
    # and show typical implementation.
    models_factory = None
    
    # factory of actor class
    # it should be able to create an actor class once an workflow
    # is instantiated.
    # and this class will be placed into the "actors" sub-package
    # of the application to handle requests.
    actor_factory = None

    # factory of visuals
    visual_factory = None
    

    def __init__(self):
        # create models if necessary
        self.createModels()

        #
        self._configureActorFactory()
        self._configureVisualFactory()
        return


    @property
    def visuals(self):
        return self.visual_factory
    

    @classmethod
    def createModels(cls):
        cls.models_factory()
        return


    # lazy creation of property "Actor"
    @property
    def Actor(self):
        # see also: _configureActorFactory
        try: return self._Actor
        except AttributeError:
            a = self._Actor = self.actor_factory()
            return a


    @classmethod
    def singleton_factory(cls, f):
        """convert a factory method to a factory that creates
        only one instance
        """
        def _():
            # XXX: should we consider keeping a week reference to the
            # XXX: instance in the Workflow class?
            if not hasattr(f, 'instance'):
                f.instance = f()
            return f.instance
        return _
    # an alias
    factory = singleton_factory


    def _configureActorFactory(self):
        """This method should be overloaded by the subclass.
        And it should configure the actor factory so that
        the factory can instantiate an actor class without any
        arguments:

          Actor = self.actor_factory()
          
        """
        raise NotImplementedError


    def _configureVisualFactory(self):
        """This method should be overloaded by the subclass.
        And it should configure the visual factory.
        """
        raise NotImplementedError


# End of file 
