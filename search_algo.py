import abc;

import state
import heuristic

class SearchAlgo():

    def __init__(self, initial_state:state.State, _heuristic:heuristic.Heuristic):
        self.open_list = list[state.State]
        self.closed_list =  list[state.State]
        self.heuristic = _heuristic
        #other variables to store performance

    @abc.abstractmethod
    def execute():
        pass


class BreadthFirst(SearchAlgo):

    def execute():
        pass
