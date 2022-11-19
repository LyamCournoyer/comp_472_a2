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

    def move_vehicle(self, name:str, times:int):
        for v in self.vehicle_list:
            if v.name == name:
                v.move(times)
                self.gen_map_2darray(self)
    
    def can_vehicle_move(self, name:str, times:int):
        for v in self.vehicle_list:
            if v.name == name:
                new_position_list = v.get_pos_list_if_moved(times)
                for pos in new_position_list:
                    x = pos[0]
                    y = pos[1]

                    if (x < 0 or x >= self.x_len) or (y < 0 or y >= self.y_len):
                        return False
                    if self.map_array[x][y] != '.' and self.map_array[x][y] != v.name:
                        return False
        return True
        
    def __str__(self):
        # create an input map string  i.e AAABCDFEEBCDF.RRC.GGH....IH.KK.IJJLL
        string = ""
        for row in range(self.x_len):
            for col in range(self.y_len):
                string+=self.map_array[row][col]

        for v in self.vehicle_list:
            if v.gas != 100:
                string = '{} {}{}'.format(string, v.name, v.gas)
        return str(string)