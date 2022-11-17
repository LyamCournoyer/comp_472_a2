import abc
import game_map


class Heuristic(abc.ABC):
    
    def get_heuristic(game_map:game_map.GameMap):
        pass

class h1(Heuristic):
    def get_heuristic(game_map:game_map.GameMap):        
        found_vehicles = []
        h = 0
        for i in reversed(range(game_map.x_len)):
            map_entry = game_map.map_array[2][i]
            if map_entry == 'A':
                break
            elif map_entry != '.' and map_entry not in found_vehicles:
                h += 1
                found_vehicles.append(map_entry)

        return h
        
    def __str__():
        return 'h1'

class h2(Heuristic):
    def get_heuristic(game_map:game_map.GameMap):
      
        h = 0
        for i in reversed(range(game_map.x_len)):
            map_entry = game_map.map_array[2][i]
            if map_entry == 'A':
                break
            elif map_entry != '.':
                h += 1
        return h


    def __str__():
        return str('h2')

class h3(Heuristic):
    MULTIPLIER = 5
    def get_heuristic(game_map:game_map.GameMap):
        return h1.get_heuristic(game_map) * h3.MULTIPLIER
        
    def __str__():
        return str('h3')