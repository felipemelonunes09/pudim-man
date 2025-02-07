from __future__ import annotations
from enum import Enum

class StateManager():
    class State(Enum):
        RUNNING = 1
        QUESTIONING = 2
        EXITING = 3
        
    def __init__(self, state: State):
        self.__state = state

    def getState(self) -> State:
        return self.__state
    
    def setState(self, state: State):
        self.__state = state

