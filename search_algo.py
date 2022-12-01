import abc;
from queue import PriorityQueue
import time
import state
import game_map
import heuristic

class SearchAlgo():

    def __init__(self, _initial_state:state.State, _heuristic:heuristic.Heuristic):
        self.start_time = 0
        self.end_time = 0
        self.open_list = PriorityQueue()
        self.closed_list =  list[state.State]
        self.visited_list = list[state.State]
        self.heuristic = _heuristic
        self.initial_state = _initial_state
        self.state_count = 0

    @abc.abstractmethod
    def execute(self):
        pass

class UniformCost(SearchAlgo):
    def __init__(self, _initial_state:state.State):
        self.start_time = 0
        self.end_time = 0
        self.open_list = PriorityQueue()
        self.visited_list = list()
        self.initial_state = _initial_state
        self.move_list = {}
        self.state_count = 0

    def execute(self, search_file):
        self.start_time = time.time()
        # insert root node
        entry_count = 0
        self.open_list.put((0, entry_count, {'new_state':self.initial_state.get_map().__str__()}))

        # until goal is reached check status
        while not self.open_list.empty():
            # pop & setup info needed
            node_tuple = self.open_list.get()
            current_node = node_tuple[2]
            current_state = state.State(current_node['new_state'])
            current_cost = node_tuple[0]
            current_state_str = game_map.GameMap.stripped_map_string(current_node['new_state'])
            
            # Log as state being searched
            self.state_count+=1
            search_file.format_state(current_cost, 0, current_state)

            # Check state
            if current_state.is_goal_state():
                # Solution found
                self.end_time = time.time()
                return self.gen_move_list(current_node)
            elif current_state_str not in self.visited_list:
                self.move_list[current_node['new_state']] = current_node
                # enqueue children with cost
                for child in current_state.get_move_list():
                    priority = current_cost+child['cost']
                    entry_count +=1
                    self.open_list.put((priority, entry_count, child))
                
                self.visited_list.append(current_state_str)
        
        # No solution
        self.end_time = time.time()

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

    def __str__(self):
        return str('ucs') 

class GreedyBestFirst(SearchAlgo):
    def __init__(self, _initial_state:state.State, _heuristic:heuristic.Heuristic):
        self.start_time = 0
        self.end_time = 0
        self.open_list = PriorityQueue()
        self.visited_list = list()
        self.initial_state = _initial_state
        self.heuristic = _heuristic
        self.move_list = {}
        self.state_count = 0

    def execute(self, search_file):
        self.start_time = time.time()
        # root node
        entry_count = 0
        self.open_list.put((0, entry_count, {'new_state':self.initial_state.get_map().__str__()}))

        while not self.open_list.empty():
            # pop
            node_tuple = self.open_list.get()
            current_node = node_tuple[2]
            hn = node_tuple[0]
            current_state = state.State(current_node['new_state'])
            current_state_str = game_map.GameMap.stripped_map_string(current_node['new_state'])
            
            # Log as state being searched
            self.state_count+=1
            search_file.format_state(0, hn, current_state)

            if current_state.is_goal_state():
                # Solution found
                self.end_time = time.time()
                return self.gen_move_list(current_node)
            elif current_state_str not in self.visited_list:
                self.move_list[current_node['new_state']] = current_node
                # enqueue children with heuristic
                for child in current_state.get_move_list():
                    priority = self.heuristic.get_heuristic(state.State(child['new_state']).get_map())
                    entry_count +=1
                    self.open_list.put((priority, entry_count, child))
                
                self.visited_list.append(current_state_str)

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

    def __str__(self):
        return f'gbfs-{self.heuristic.__str__()}'

class  A(SearchAlgo):
    def __init__(self, _initial_state:state.State, _heuristic:heuristic.Heuristic):
        self.start_time = 0
        self.end_time = 0
        self.name = "a"
        self.open_list = {}
        self.closed_list =  {}
        self.move_list = {} #k:state, v:move
        self.g_score = {} #k:state, v:score
        self.heuristic = _heuristic
        self.initial_state = _initial_state        
        self.g_score[_initial_state.get_map().__str__().split()[0]] = 0
        self.open_list[_initial_state.get_map().__str__().split()[0]] = self.heuristic.get_heuristic(_initial_state.get_map())
        self.move_list[_initial_state.get_map().__str__().split()[0]] = {'new_state': _initial_state.get_map().__str__(), 'cost':0, 'parent':None}
        self.state_count = 0
      
    def execute(self, search_file):
        self.start_time = time.time()
        while self.open_list:
            self.open_list = {k: v for k, v in sorted(self.open_list.items(), key=lambda item: item[1])}
            current_state_str = next(iter(self.open_list))            
            fn = self.open_list.pop(current_state_str)
            full_state_str = self.move_list[current_state_str]['new_state']
            
            current_state = state.State(full_state_str)
            self.state_count += 1
            gn = self.g_score[current_state_str]
            search_file.format_state(gn, fn-gn, current_state)

            if current_state.get_map().is_goal_reached():
                self.end_time = time.time()
                return self.gen_move_list(self.move_list[current_state_str])
            for move in current_state.get_move_list():
                tmp_g_score = self.g_score[current_state_str] + move['cost']
                if (move['new_state'].split()[0] in self.g_score.keys() and tmp_g_score < self.g_score[move['new_state'].split()[0]]) or move['new_state'].split()[0] not in self.g_score.keys():
                        self.move_list[move['new_state'].split()[0]] = move
                        self.g_score[move['new_state'].split()[0]] = tmp_g_score
                        self.open_list[move['new_state'].split()[0]] = tmp_g_score + self.heuristic.get_heuristic(state.State(move['new_state']).get_map())           
                    
        return None
                    
    def gen_move_list(self, finale_move):
        move = finale_move
        move_list = []
        while True:
            if move['parent'] == self.initial_state.get_map().__str__():
                move_list.insert(0,move)
                break
            move_list.insert(0,move)
            move = self.move_list[move['parent'].split()[0]]
        
        return move_list

    def __str__(self):
        return str('a')+self.heuristic.__str__()
    
        