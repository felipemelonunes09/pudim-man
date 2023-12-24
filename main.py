from core.GameEngine import *
from core.GameProxy import *

global proxy

if __name__ == '__main__': 

    game = GameEngine()
    GameProxy.set_context(GameEngine)

    game.start()

