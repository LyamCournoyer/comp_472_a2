import unittest
import state
import heuristic

class TestHeuristics(unittest.TestCase):
    STATES_TO_TEST = [        
        {'name':  "IIB...C.BHHHC.AAD.....D.EEGGGF.....F", 'h1_expected':1, 'h2_expected': 1,},
        {'name':  "C.B...C.BHHHAADD........EEGGGF.....F", 'h1_expected':1, 'h2_expected': 2},
        {'name':  "...GF...BGF.AABCF....CDD...C....EE..", 'h1_expected':3, 'h2_expected': 3},
        {'name':  ".......C.BHHHC...AA...D.EEGGGF.....F", 'h1_expected':0, 'h2_expected': 0,},
       
    ]
    for e in STATES_TO_TEST:
        e['h3_expected'] = e['h1_expected'] * heuristic.h3.MULTIPLIER

    def test_h1(self):
        self.run_test(heuristic.h1, 'h1_expected')
    
    def test_h2(self):
        self.run_test(heuristic.h2, 'h2_expected')
    
    def test_h3(self):
        self.run_test(heuristic.h3, 'h3_expected')

    def run_test(self, heuristic_, expected_str):
        
        for state_line in self.STATES_TO_TEST:
            with self.subTest('{} on {}'.format(heuristic_.__str__(),state_line['name'] )):
                state_ = state.State(state_line['name']) 
                res = heuristic_.get_heuristic(state_.game_map)
                self.assertEqual(res, state_line[expected_str])


if __name__ == '__main__':
    unittest.main()            