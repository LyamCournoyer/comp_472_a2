import state
import game_map
import search_algo
import heuristic

def main():
    input_file = "sample_files\Sample\sample-input.txt"
    state_list = parse_input_file(input_file)
    # heuristic_list = list[heuristic.Heuristic]
    # heuristic_list.append(heuristic.h1())
    for game in state_list:
        run_a(state_list, [heuristic.h1])
        run_ucs(state_list)

def parse_input_file(file_path:str) -> list[state.State]:
    valid_lines = list[state.State]()
    with open(file_path) as file:
        lines = file.readlines()
        for line in lines:
            # Is valid line?
            line = line.strip()
            if(line and not line.startswith('#')):                
                valid_lines.append(state.State(line))
    return valid_lines

def run_a(state_list, heuristic_list):
    for _heuristic in heuristic_list:
        for item in state_list:            
            algo = search_algo.A(item, _heuristic)
            algo.execute()

def run_ucs(state_list):
    for item in state_list:
        algo = search_algo.UniformCost(item, 0)
        res = algo.execute()
        print("solution found in " + str(len(res)) + " moves")



if __name__ == "__main__":
    main()