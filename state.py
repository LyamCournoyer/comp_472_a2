
import game_map 
import vehicle

class State:
    
    """
    
    """
    def __init__(self, line:str):
        #should be a valide setup line. See the project handout for details
        #i.e AAB...C.BHHHC.RRDF....DFEEGGG....... D0
        SIZE = 6
        #iterate string and generate vehicle list ... create required vehicles and set their gas
        cars={}
        ind = 0
        for row in range(SIZE):
            for col in range(SIZE):
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
        self.game_map = game_map.GameMap(SIZE*SIZE, self.vehicle_list)
        pass

    def __str__(self):
        #should generate the same string that is used to initate the map
        return '{} {}'.format(self.game_map.__str__(), self.vehicle_list.__str__())

    def get_map(self) -> game_map.GameMap:
        return self.game_map

    