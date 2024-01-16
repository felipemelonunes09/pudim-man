from typing import List
from core.objects.ship.rooms.room import Room, ROOM_TYPE
from core.objects.ship.objects.Generator import Generator

class PowerRoom(Room):
    
    def __init__(self, generators = List[Generator]) -> None:

        super().__init__(ROOM_TYPE)

        self.power_supply = 0
        self.generators = generators
        
    def activate_all_generator(self):
        for g in self.generators:
            g.activate()

    def deactivate_all_generators(self):
        for g in self.generators:
            g.deactivate()

    def increase_all_generator_usage(self, value: float):
        for g in self.generators:
            g.increase_usage(value)

    def decrease_all_generator_usage(self, value: float):
        for g in self.generators:
            g.decrease_usage(value)
            
    def generate_power(self):
        self.power_supply = 0
        for g in self.generators:
            self.power_supply += g.work()
    
    def get_power_supply(self) -> float:
        return self.power_supply
            


    

    

        