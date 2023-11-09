class Player:
    def __init__(self, action: int):
        self._action = action

    # Getters and setters

class Action:
    _target = None
    _actor = None

    # Getters and setters

    def __init__(self, actor: int, target: int):
        self.setActor(actor)
        self.setTarget(target)

class GameState:
    players = []
    
    def player(self, id : int) -> Player:
        if (id < 0 or id >= 128):
            return None
        return self.players[id]        
    