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
    def __init__(self, _initial_state:state.State, _heuristic:heuristic.Heuristic):
        self.open_list = PriorityQueue()
        self.visited_list = list()
        self.heuristic = _heuristic
        self.initial_state = _initial_state
        self.move_list = {}

    def execute(self):
        # insert root node
        entry_count = 0
        self.open_list.put((0, entry_count, {'new_state':self.initial_state.get_map().__str__()}))

        # until goal is reached check status
        while not self.open_list.empty():
            # pop
            node_tuple = self.open_list.get()
            current_node = node_tuple[2]
            current_state = state.State(current_node['new_state'])
            current_cost = node_tuple[0]
            if current_state.is_goal_state():
                # print info?
                return self.gen_move_list(current_node)
            elif current_node['new_state'] not in self.visited_list:
                self.move_list[current_node['new_state']] = current_node
                # enqueue children with cost
                for child in current_state.get_move_list():
                    priority = current_cost+child['cost']
                    entry_count +=1
                    self.open_list.put((priority, entry_count, child))
                
                self.visited_list.append(current_node['new_state'])

    def gen_move_list(self, finale_move):
        move = finale_move
        move_list = []
        while True:
            if move['parent'] == self.initial_state.get_map().__str__():
                move_list.insert(0,move)
                break
            move_list.insert(0,move)
            move = self.move_list[move['parent']]
          
        return move_list


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
        self.g_score[_initial_state.get_map().__str__()] = 0
        self.open_list[_initial_state.get_map().__str__()] = self.heuristic.get_heuristic(_initial_state.get_map())
      


    def execute(self):
        while self.open_list:
            self.open_list = {k: v for k, v in sorted(self.open_list.items(), key=lambda item: item[1])}
            current_state_str = next(iter(self.open_list))            
            self.open_list.pop(current_state_str)
            current_state = state.State(current_state_str)
            if current_state.get_map().is_goal_reached():
                return self.gen_move_list(self.move_list[current_state_str])
            for move in current_state.get_move_list():
                tmp_g_score = self.g_score[current_state_str] + move['cost']
                if move['new_state'] in self.g_score.keys():
                    if tmp_g_score < self.g_score[move['new_state']]:
                        self.move_list[move['new_state']] = move
                        self.g_score[move['new_state']] = tmp_g_score
                        self.open_list[move['new_state']] = tmp_g_score + self.heuristic.get_heuristic(state.State(move['new_state']).get_map())
                if move['new_state'] not in self.g_score.keys():
                    self.move_list[move['new_state']] = move
                    self.g_score[move['new_state']] = tmp_g_score
                    self.open_list[move['new_state']] = tmp_g_score + self.heuristic.get_heuristic(state.State(move['new_state']).get_map())

                    
        return None
                    
                    
    def gen_move_list(self, finale_move):
        move = finale_move
        move_list = []
        while True:
            if move['parent'] == self.initial_state.get_map().__str__():
                move_list.insert(0,move)
                break
            move_list.insert(0,move)
            move = self.move_list[move['parent']]
          
        return move_list

                
             
            
    def in_queue(self, str, queue):
        while not queue.empty():
            if str == queue.get():
                return(True)

    

        