import abc
import search_algo
import state
import game_map
import heuristic

class OutputFile(abc.ABC):
    puzzle_number = 1

    @abc.abstractmethod
    def generate_file(self):
        pass

class SearchFile(OutputFile):
    
    def __init__(self, _initial_state:state.State, _search:search_algo.SearchAlgo):
        self.filename = _search.__str__() + str(OutputFile.puzzle_number)

    def generate_file(self):
        with open(self.filename, 'w') as f:
            pass
        


class SolutionFile(OutputFile):
   
    def __init__(self, _initial_state:state.State, _search:search_algo.SearchAlgo, _solution:list = None):
        self.filename = f'{_search.__str__()}-sol-{str(OutputFile.puzzle_number)}'
        OutputFile.puzzle_number+=1
        self.initial_state = _initial_state
        self.solution_list = _solution
        self.search = _search
    
    def generate_file(self):
        map = self.initial_state.get_map()
        map_conf = map.gen_map_2darray()
        with open(self.filename, 'w') as f:
            # Case no solution
            if self.solution_list is None:
                f.write('No solution')
                return

            # Initial configuration
            f.write(f'Initial board configuration: {map.__str__()}')
            f.write('\n\n')
            for row in map_conf:
                for elem in row:
                    f.write(elem)
                f.write('\n')
            f.write('\n')
            f.write('Car fuel available: ')
            for car in map.vehicle_list:
                f.write(f'{car.name}:{car.gas}, ')

            # Solution info
            f.write('\n\n')
            f.write(f'Runtime: {round((self.search.end_time-self.search.start_time), 3)} seconds\n')
            f.write(f'Search path length: \n')
            f.write(f'Solution path length: {len(self.solution_list)}\n')
            solution_str = 'Solution Path: '
            solution_states_str = ''

            for ind in range(len(self.solution_list)):
                solution_str+=f"{self.solution_list[ind]['vehicle_name']} {self.solution_list[ind]['direction']} {abs(self.solution_list[ind]['times'])}"
                solution_str+= "\n" if ind == len(self.solution_list)-1  else "; "
                
                solution_states_str+=f"{self.solution_list[ind]['vehicle_name']}\t{self.solution_list[ind]['direction']: >5}\t{abs(self.solution_list[ind]['times']): >2}{self.solution_list[ind]['gas_left']: >10} {game_map.GameMap.stripped_map_string(self.solution_list[ind]['new_state'])}\n"

            f.write(solution_str)  
            f.write('\n\n')
            f.write(solution_states_str)
