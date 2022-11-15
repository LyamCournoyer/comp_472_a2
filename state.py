
import game_map 
import vehicle

class State:
    """
    
    """
    def __init__(self, line:str):
        #should be a valide setup line. See the project handout for details
        #i.e AAB...C.BHHHC.RRDF....DFEEGGG....... D0

        #iterate string and generate vehicle list ... create required vehicles and set their has
        self.vehicle_list = list[vehicle.Vehicle]
        # generate a map for this state
        self.game_map = game_map.GameMap(36, self.vehicle_list)
        pass

    def __str__(self):
        #should generate the same string that is used to initate the map
        return '{} {}'.format(self.game_map.__str__(), self.vehicle_list.__str__())

    def get_map(self) -> game_map.GameMap:
        return self.game_map

    