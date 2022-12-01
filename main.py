import state
import game_map
import output
import search_algo
import heuristic

def main():
    input_file = "sample_files\Sample\sample-input.txt"
    state_list = parse_input_file(input_file)
    heuristic_list = [heuristic.h1, heuristic.h2, heuristic.h3]
   
    run_ucs(state_list)
    run_gbfs(state_list, heuristic_list)
    # run_a(state_list, heuristic_list)

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
    output.OutputFile.puzzle_number = 1
    for item in state_list:
        for _heuristic in heuristic_list:        
            # setup  
            algo = search_algo.A(item, _heuristic)
            search_file = output.SearchFile(algo)

            # run search
            solution_path = algo.execute(search_file)

            # output
            search_file.generate_file()
            result_file = output.SolutionFile(item, algo, solution_path) 
            result_file.generate_file()
        output.OutputFile.puzzle_number += 1

def run_ucs(state_list):
    output.OutputFile.puzzle_number = 1
    for item in state_list:
        # setup
        algo = search_algo.UniformCost(item)
        search_file = output.SearchFile(algo)
        
        # run search
        solution_path = algo.execute(search_file)
        
        # output   
        search_file.generate_file()
        result_file = output.SolutionFile(item, algo, solution_path) 
        result_file.generate_file()
        output.OutputFile.puzzle_number += 1
    

def run_gbfs(state_list, heuristic_list):
    output.OutputFile.puzzle_number = 1
    for item in state_list:
        for _heuristic in heuristic_list:
            # setup
            algo = search_algo.GreedyBestFirst(item, _heuristic)
            search_file = output.SearchFile(algo)

            # run search
            solution_path = algo.execute(search_file)

            # output
            search_file.generate_file()
            result_file = output.SolutionFile(item, algo, solution_path) 
            result_file.generate_file()
        output.OutputFile.puzzle_number += 1

if __name__ == "__main__":
    main()