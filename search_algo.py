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



class  A(SearchAlgo):
    def __init__(self, _initial_state:state.State, _heuristic:heuristic.Heuristic):
        self.open_list = {}
        self.closed_list =  {}
        self.move_list = {} #k:state, v:move
        self.g_score = {} #k:state, v:score
        self.heuristic = _heuristic
        self.initial_state = _initial_state        
        self.g_score[_initial_state.get_map().__str__().split()[0]] = 0
        self.open_list[_initial_state.get_map().__str__().split()[0]] = self.heuristic.get_heuristic(_initial_state.get_map())
        self.move_list[_initial_state.get_map().__str__().split()[0]] = {'new_state': _initial_state.get_map().__str__(), 'cost':0, 'parent':None}
      


    def execute(self):
        while self.open_list:
            self.open_list = {k: v for k, v in sorted(self.open_list.items(), key=lambda item: item[1])}
            current_state_str = next(iter(self.open_list))            
            self.open_list.pop(current_state_str)
            full_state_str = self.move_list[current_state_str]['new_state']
            
            current_state = state.State(full_state_str)
            if current_state.get_map().is_goal_reached():
                return self.gen_move_list(self.move_list[current_state_str])
            for move in current_state.get_move_list():
                tmp_g_score = self.g_score[current_state_str] + move['cost']
                if (move['new_state'].split()[0] in self.g_score.keys() and tmp_g_score < self.g_score[move['new_state'].split()[0]]):
                        self.move_list[move['new_state'].split()[0]] = move
                        self.g_score[move['new_state'].split()[0]] = tmp_g_score
                        self.open_list[move['new_state'].split()[0]] = tmp_g_score + self.heuristic.get_heuristic(state.State(move['new_state']).get_map())
                if move['new_state'].split()[0] not in self.g_score.keys():
                    self.move_list[move['new_state'].split()[0]] = move
                    self.g_score[move['new_state'].split()[0]] = tmp_g_score
                    self.open_list[move['new_state'].split()[0]] = tmp_g_score + self.heuristic.get_heuristic(state.State(move['new_state']).get_map())

                    
        return None
                    
                    
    def gen_move_list(self, finale_move):
        move = finale_move
        move_list = []
        while True:
            if not move['parent']:
                move_list.insert(0,move)
                break
            move_list.insert(0,move)
            move = self.move_list[move['parent'].split()[0]]
        
        return move_list

        