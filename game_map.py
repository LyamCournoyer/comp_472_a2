import vehicle
import math
class GameMap:

    def __init__(self, size:int, vehicle_list):
        self.x_len = int(math.sqrt(size))
        self.y_len = int(math.sqrt(size))
        self.vehicle_list = vehicle_list
        self.map_array = self.gen_map_2darray()

    def gen_map_2darray(self):
        #create an x by empty array
        map_arr = [["."] * self.x_len for i in range(self.y_len)]
        
        for v in self.vehicle_list:
            #fill the empty spaces with vehicles   
            for pos in v.get_positions():
                map_arr[pos[0]][pos[1]] = v.get_name()       

        return map_arr

    def is_location_empty(self, x:int, y:int):
        pass
    
    def is_goal_reached(self): 
        return self.map_array[2][5] == 'A'


    def move_vehicle(self, name:str, times:int):
        for v in self.vehicle_list:
            if v.name == name:
                v.move(times)
                self.gen_map_2darray(self)
    
    def can_vehicle_move(self, name:str, times:int):
        for v in self.vehicle_list:
            if v.name == name:
                #new_position_list = v.get_pos_list_if_moved(times)
                if v.gas < abs(times):
                    return False
                for pos in v.pos:
                    x = pos[0]
                    y = pos[1]
                    if times < 0:
                        r =  range(times,0)
                    else:
                        r = range(1,times+1)
                    for t in r:
                        move_dir = v.determine_move_direction()
                        new_x = x + t * move_dir[0]
                        new_y = y + t * move_dir[1]
                        if (new_x < 0 or new_x >= self.x_len) or (new_y < 0 or new_y >= self.y_len):
                            return False
                        if self.map_array[new_x][new_y] != '.' and self.map_array[new_x][new_y] != v.name:
                            return False
        return True

    def stripped_map_string(map_str):
        return map_str[0:36]

    def __str__(self):
        # create an input map string  i.e AAABCDFEEBCDF.RRC.GGH....IH.KK.IJJLL
        string = ""
        for row in range(self.x_len):
            for col in range(self.y_len):
                string+=self.map_array[row][col]

        for v in sorted(self.vehicle_list, key=lambda x: x.name):
            if v.gas != 100:
                string = '{} {}{}'.format(string, v.name, v.gas)
        return str(string)