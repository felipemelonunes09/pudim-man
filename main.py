from core.GameEngine import *
from core.GameProxy import *


if __name__ == '__main__': 

    game = GameEngine()
    GameProxy.set_context(GameEngine)

    game.start()

