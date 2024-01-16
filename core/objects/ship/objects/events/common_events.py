
from core.general.events.Event import Event

"""
MECHANICAL_BREAK_LOW
"""

class MechanicalBreakLow(Event):
    pass

class MechanicalBreakMedium(Event):
    pass

class MechanicalBreakHigh(Event):
    pass

class StartFireEvent(Event):
    pass

class OnFireEvent(Event):
    pass

COMMON_EVENTS = [
    MechanicalBreakLow,
    MechanicalBreakMedium,
    MechanicalBreakHigh,
    StartFireEvent,
    OnFireEvent
]

COMMON_EVENTS_DICT = {}

for event in COMMON_EVENTS:
    COMMON_EVENTS_DICT[event.__name__] = event