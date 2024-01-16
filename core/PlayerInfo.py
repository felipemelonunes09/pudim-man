

from core.Player import Player

class PlayerInfo():

    @staticmethod
    def get_player_ship_basic_info(player: Player):
        
        return {
            "speed": 100,
            "power": player.power_room.get_power_supply()
        }