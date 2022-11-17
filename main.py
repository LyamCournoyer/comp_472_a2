import state
import game_map

def main():
    input_file = "sample_files\Sample\sample-input.txt"
    state_list = parse_input_file(input_file)

    for state_line in state_list:
        print(state_line.get_map().__str__())
    # heuristic_list = list[heuristic.Heuristic]
    # heuristic_list.append(heuristic.h1())



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


# def run_breadth_first(state_list:list[str], heuristic_list = list[heuristic.Heuristic]):
#     for _heuristic in heuristic_list:
#         for item in state_list:
            
#             algo = search_algo.BreadthFirst(state.State(item), _heuristic)

if __name__ == "__main__":
    main()