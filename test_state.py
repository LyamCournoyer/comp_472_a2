import unittest
import state

class TestState(unittest.TestCase):

    STATES_TO_TEST_WITH_1_MOVE = [                
        {'name': '1_moves_no_conflicts', 'initial_state': '.II.................................', 'expected_states': ['II.................................. I99', '..II................................ I99']},
        {'name': '1_moves_no_conflicts_2_vehicles', 'initial_state': '.II.............D.....D............. D11', 'expected_states': ['.II...................D.....D....... D10' , '.II.......D.....D................... D10', 'II..............D.....D............. D11 I99', '..II............D.....D............. D11 I99']},
        {'name': 'blocked_vehicle', 'initial_state':      'IIDD................................ D11', 'expected_states': ['II.DD............................... D10']},
        {'name': '1_vehicle_no_gas', 'initial_state': '.II.............D.....D............. D0', 'expected_states': ['II..............D.....D............. D0 I99', '..II............D.....D............. D0 I99']},
    ]
    
    STATES_TO_TEST_WITH_2_MOVE = [                
        {'name': '2_moves_horizontal', 'initial_state': '.II.................................', 'expected_states': ['...II............................... I98' , 'II.................................. I99', '..II................................ I99']},       
    ]
 
    def test_get_move_list_with_1_move(self):  
        state.State.MOVES_TO_MAKE = [-1, 1]      
        for state_to_test in TestState.STATES_TO_TEST_WITH_1_MOVE:
            with self.subTest(state_to_test['name']):
                state_ = state.State(state_to_test['initial_state'])
                move_list = state_.get_move_list()
                self.assertEqual(len(move_list), len(state_to_test['expected_states']))
                for move in move_list:
                    self.assertIn(move['new_state'], state_to_test['expected_states'])  # Should probably just be a set diff   
            

    def test_get_move_list_with_max_2_moves(self):  
        state.State.MOVES_TO_MAKE = [-2, -1 , 1, 2]      
        for state_to_test in TestState.STATES_TO_TEST_WITH_2_MOVE:
            with self.subTest(state_to_test['name']):
                state_ = state.State(state_to_test['initial_state'])
                move_list = state_.get_move_list()
                self.assertEqual(len(move_list), len(state_to_test['expected_states']))
                for move in move_list: 
                    self.assertIn(move['new_state'], state_to_test['expected_states'])  # Should probably just be a set diff   
        
     
if __name__ == '__main__':
    unittest.main()            

