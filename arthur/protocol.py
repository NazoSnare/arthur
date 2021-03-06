"""The arthur AMP protocol and factory.

"""
from arthur.exercises import ExercisesLocator
from twisted.internet.protocol import ReconnectingClientFactory
from twisted.protocols.amp import AMP


class Protocol(AMP):
    """The arthur AMP protocol.

    """
    def __init__(self):
        AMP.__init__(self, locator=ExercisesLocator(self))



class Factory(ReconnectingClientFactory):
    protocol = Protocol

    def __init__(self, workbench):
        self.workbench = workbench
