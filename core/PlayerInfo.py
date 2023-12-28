

from core.Player import Player

class PlayerInfo():

    @staticmethod
    def get_player_ship_basic_info(player: Player):
        return {
            "speed": player.motorRoom.get_avarage_using()
        }