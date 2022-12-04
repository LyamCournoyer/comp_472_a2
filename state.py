
import game_map 
import vehicle

class State:
    
    MOVES_TO_MAKE = [-4, -3, -2 ,-1 , 1, 2, 3, 4]
    EXIT_POSITION = [2, 5]
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
        
        #Set gas
        gas_list = line.split()[1:]
        for entry in gas_list:
            car_name = entry[0]
            gas = int(entry[1:])
            for v in self.vehicle_list:
                if v.name == car_name:
                    v.gas = gas

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
        for spaces_to_move in State.MOVES_TO_MAKE:
            for vehicle_to_move in self.game_map.vehicle_list:
                if self.game_map.can_vehicle_move(vehicle_to_move.name, spaces_to_move):
                    move = {}
                    move['vehicle_name'] = vehicle_to_move.name
                    move['gas_left'] = vehicle_to_move.gas - abs(spaces_to_move)
                    move['direction'] = vehicle_to_move.move_dir_to_str(spaces_to_move)
                    move['times'] = spaces_to_move
                    move['new_state'] = self.gen_state_with_new_vehicle_pos(vehicle_to_move, spaces_to_move)
                    move['parent'] = self.get_map().__str__()
                    move['cost'] = 1
                    move_list.append(move)
        return move_list
                 
    def gen_state_with_new_vehicle_pos(self, vehicle_to_move, spaces_to_move):
        tmp_v_list = []
        
        for v in self.vehicle_list:
            if v.name == vehicle_to_move.name:
                tmp_v = vehicle.Vehicle(v.name)
                
                for pos in v.pos:
                    tmp_v.add_pos(pos[0], pos[1])
                tmp_v.gas = v.gas
                tmp_v.move(spaces_to_move)

                if not self.vehicle_can_leave(tmp_v):
                    tmp_v_list.append(tmp_v)
                
            else: 
                tmp_v_list.append(v)
        
        return game_map.GameMap(State.MAP_SIZE*State.MAP_SIZE, tmp_v_list).__str__()
 
    def vehicle_can_leave(self, v:vehicle.Vehicle):
        for pos in v.get_positions():
            # Vehicle must be at exit and move left/right
            if pos == State.EXIT_POSITION and v.determine_move_direction == [1,0] and v.get_name() != "A":
                return True

        return False 

    def is_goal_state(self):
        return self.game_map.is_goal_reached()

    def get_ambo_gas(self):
        for v in self.vehicle_list:
            if v.name == 'A':
                return v.gas
        