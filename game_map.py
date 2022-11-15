import vehicle
import math
class GameMap:
    def __init__(self, size:int, vehicle_list:list[vehicle.Vehicle]):
        self.x_len = math.sqrt(size)
        self.y_len = math.sqrt(size)
        self.vehicle_list = vehicle_list
        self.map_array = self.gen_map_2darray()

    def gen_map_2darray():
        #create an x by empty array

        #fill the empty spaces with vehicles
        pass

    def is_location_empty(self, x:int, y:int):
        pass

    def move_vehicle(self, name:str, times:int):
        for v in self.vehicle_list:
            if v.name == name:
                v.move(times)
                self.gen_map_2darray()
                
        pass
    def __str__(self):
        # create an input map string  i.e AAABCDFEEBCDF.RRC.GGH....IH.KK.IJJLL 
        pass