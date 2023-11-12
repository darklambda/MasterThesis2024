import example as module_0
import dependencies as module_1

def test_case_0():
    basic_rules_0 = module_0.BasicRules()
    int_0 = 253
    int_1 = 128
    action_0 = module_1.Action(int_0, int_1)
    game_state_0 = module_1.GameState()
    players = []
    int_3 = 32
    player_0 = module_1.Player(int_3)
    players.append(player_0)
    game_state_0.setPlayers(players)
    int_4 = 372
    player_1 = game_state_0.player(int_4)
    int_5 = 921
    player_1.setAction(int_5)
    bool_0 = basic_rules_0.checkRules(action_0, game_state_0)
