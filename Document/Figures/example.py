from dependencies import GameState, Player, Action

class BasicRules:
    def checkRules(self, action: Action, state: GameState) -> bool:
        actor: Player = state.player(action.getActor())
        target: Player = state.player(action.getTarget())

        if actor == None:
            return False
        if target == None:
            return False
        if actor.getAction() == 1:
            return True