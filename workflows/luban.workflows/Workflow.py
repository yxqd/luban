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
    These models are the foundatioin, the things to be manipulated
    in the workflow.
    For example, a login workflow at the least needs a "users" table.

    then, a workflow consists of an actor (should we consider multiple
    actors. let us keep it simple for now), and a visual factory that
    knows how to create visuals related to this workflow.

    Once created, a work
    self.actor is the actor class for this workflow

    typically
    1. create a customized workflow in a module
      >>> from somewhere import Workflow
      >>> workflow = Workflow(...)

    2. in the actor module:
      >>> from workflow_module import workflow
      >>> class Actor(workflow.Actor): ...

    3. when creating a visual:
      >>> from workflow_module import workflow
      >>> form = workflow.visuals.form(...)
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


    # lazy creation of property "actor"
    @property
    def Actor(self):
        # see also: _configureActorFactory
        try: return self._Actor
        except:
            a = self._Actor = self.actor_factory()
            return a


    def _configureActorFactory(self):
        """This method should be overloaded by the subclass.
        And it should configure the actor factory so that
        the factory can instantiate an actor class without any
        arguments:

          Actor = self.createActor()
          
        """
        raise NotImplementedError


    def _configureVisualFactory(self):
        """This method should be overloaded by the subclass.
        And it should configure the visual factory.
        """
        raise NotImplementedError


# End of file 
