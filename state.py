
import game_map 
import vehicle

class State:
    
    """
    
    """
    MAP_SIZE = 6
    def __init__(self, line:str):
        #should be a valide setup line. See the project handout for details
        #i.e AAB...C.BHHHC.RRDF....DFEEGGG....... D0
       
        #iterate string and generate vehicle list ... create required vehicles and set their gas
        cars={}
        ind = 0
        for row in range(State.MAP_SIZE):
            for col in range(State.MAP_SIZE):
                if(line[ind] in cars):
                    # Add to position
                    cars[line[ind]].add_pos(row,col)
                    pass
                elif (line[ind]!="."):
                    # Create new vehicle
                    car = vehicle.Vehicle(line[ind])
                    car.add_pos(row,col)
                    cars[line[ind]] = car
                    
                ind+=1

        self.vehicle_list = list(cars.values())
       
        # generate a map for this state
        self.game_map = game_map.GameMap(State.MAP_SIZE*State.MAP_SIZE, self.vehicle_list)
        pass

    def __str__(self):
        #should generate the same string that is used to initate the map
        return '{} {}'.format(self.game_map.__str__(), self.vehicle_list.__str__())

    def get_map(self) -> game_map.GameMap:
        return self.game_map

    def get_move_list(self):
        move_list = []
        times_to_move = [-1, 1]
        for spaces_to_move in times_to_move:
            for vehicle_to_move in self.game_map.vehicle_list:
                if self.game_map.can_vehicle_move(vehicle_to_move.name, spaces_to_move):
                    move = {}
                    move['vehicle_name:'] = vehicle_to_move.name
                    move['directrion'] = vehicle_to_move.move_dir_to_str(spaces_to_move)
                    move['times'] = spaces_to_move
                    move['new_state'] = self.gen_state_with_new_vehicle_pos(vehicle_to_move, vehicle_to_move.get_pos_list_if_moved(spaces_to_move))
                    move_list.append(move)
        return move_list
                
        
    def gen_state_with_new_vehicle_pos(self, vehicle_to_move, new_positions):
        tmp_v_list = []
        
        for v in self.vehicle_list:
            if v.name == vehicle_to_move.name:
                tmp_v = vehicle.Vehicle(v.name)
                tmp_v_list.append(tmp_v)
                for pos in new_positions:
                    tmp_v.add_pos(pos[0], pos[1])
            else: 
                tmp_v_list.append(v)
        
        return game_map.GameMap(State.MAP_SIZE*State.MAP_SIZE, tmp_v_list).__str__()
