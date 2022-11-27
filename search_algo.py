import abc;
from queue import PriorityQueue
import state
import heuristic

class SearchAlgo():

    def __init__(self, _initial_state:state.State, _heuristic:heuristic.Heuristic):
        self.open_list = PriorityQueue()
        self.closed_list =  list[state.State]
        self.visited_list = list[state.State]
        self.heuristic = _heuristic
        self.initial_state = _initial_state
        #other variables to store performance

    @abc.abstractmethod
    def execute(self):
        pass


class BreadthFirst(SearchAlgo):

    def execute(self):
        pass

class UniformCost(SearchAlgo):
    def execute(self):
        # insert root node
        self.open_list.put((0, self.initial_state))
        # current_node = ""
        
        # until goal is reached check status
        while not self.open_list.empty():
            # pop
            node_tuple = self.open_list.get()
            current_node = node_tuple[1]['new_state']
            current_state = state.State(current_node)
            current_cost = node_tuple[0]
            if current_state.is_goal_state():
                # print info?
                break 
            elif current_node not in self.visited_list:
                # enqueue children with cost
                for child in current_state.get_move_list():
                    self.open_list.put((current_cost+child['cost'], child))
                
                self.visited_list.append(current_node)


    def get_path():
        # Use end goal node and can get parent until initial node
        pass

class GreedyBestFirst(SearchAlgo):
    def execute(self):
        pass

    def get_path():
        # Use end goal node and can get parent until initial node
        pass