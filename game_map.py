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
                
        pass
    def __str__(self):
        # create an input map string  i.e AAABCDFEEBCDF.RRC.GGH....IH.KK.IJJLL
        string = ""
        for row in range(self.x_len):
            for col in range(self.y_len):
                string+=self.map_array[row][col]

        return str(string)