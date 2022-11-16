# import game_map
class Vehicle:
    def __init__(self, name:str, gas:int=100, is_ambo:bool=False):
        self.name = name
        self.gas = gas
        self.pos = [] # Should be a 2d array. i.e pos [[x, y], [x,4]] ... Might not need        
        self.move_dir = self.determine_move_direction() #Move vertical or horizontal.. Maybe this is decided at the end based on the position
        self.is_ambo = is_ambo; #Could sublcass but too much work at the moment

    def __eq__(self, other):
        return self.name == other.name

    def get_positions(self):
        return self.pos

    def add_pos(self, x:int, y:int):
        self.pos.append([x,y])

    def get_name(self):
        return self.name

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
        print(self.pos)

    def determine_move_direction(self):
        #determin if the vehicle can move up or down based on all of it's parts
        pass