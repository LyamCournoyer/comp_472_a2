import state
import search_algo
import heuristic
def main():
    input_file = None
    state_list = parse_input_file(input_file)
    heuristic_list = list[heuristic.Heuristic]
    heuristic_list.append(heuristic.h1())



def parse_input_file(file_path:str) -> list[str]:
    pass


def run_breadth_first(state_list:list[str], heuristic_list = list[heuristic.Heuristic]):
    for _heuristic in heuristic_list:
        for item in state_list:
            
            algo = search_algo.BreadthFirst(state.State(item), _heuristic)