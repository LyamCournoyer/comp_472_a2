import game_map
class Vehicle:
    def __init__(self, name:str, move_dir:str, gas:int=100, is_ambo:bool=False):
        self.name = name
        self.gas = gas
        self.pos = [] # Should be a 2d array. i.e pos [[x, y], [x,4]] ... Might not need        
        self.move_dir = move_dir #Move vertical or horizontal 
        self.is_ambo = is_ambo; #Could sublcass but too much work at the moment

    def add_pos(x:int, y:int, map_:game_map.GameMap):
        pass
    
    def move(n:int):
        #accept positive or negative
        #move base on move_dir... i.e down and left are negative, up and right are positve
        #if the head tile can move then so can the rest
        pass

    def is_vehicle_complete(self):
        #mainly for testing 
        #check that all positions are adjacent
        pass
    
    def __str__(self):
        #Create a vehicle to gas string. Do not output if gas is 100. i.e "C3 B4 H1"
        pass
