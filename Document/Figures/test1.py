import example as module_0
import dependencies as module_1

def test_case_0():
    basic_rules_0 = module_0.BasicRules()

def test_case_1():
    basic_rules_0 = module_0.BasicRules()
    int_0 = 253
    action_0 = module_1.Action(int_0, int_0)
    game_state_0 = module_1.GameState()
    bool_0 = basic_rules_0.checkRules(action_0, game_state_0)
