import unittest
import state

class TestState(unittest.TestCase):
    STATES_TO_TEST = [        
        {'name': 'single_move_no_conflicts', 'initial_state': '.II.................................', 'expected_states': ['II..................................', '..II................................']},         
        {'name': '2_moves_no_conflicts', 'initial_state': '.II.............D.....D.............', 'expected_states': ['.II...................D.....D.......', '.II.......D.....D...................', 'II..............D.....D.............', '..II............D.....D.............']},
    ]

    def test_get_move_list(self):
        for state_to_test in TestState.STATES_TO_TEST:
            state_ = state.State(state_to_test['initial_state'])
            move_list = state_.get_move_list()
            for move in move_list:
                self.assertIn(move['new_state'], state_to_test['expected_states'])
      
if __name__ == '__main__':
    unittest.main()            

