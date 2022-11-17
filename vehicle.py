# import game_map
class Vehicle:
    def __init__(self, name:str, gas:int=100, is_ambo:bool=False):
        self.name = name
        self.gas = gas
        self.pos = [] # Should be a 2d array. i.e pos [[x, y], [x,4]] ... Might not need                
        self.is_ambo = is_ambo; #Could sublcass but too much work at the moment

    def __eq__(self, other):
        return self.name == other.name

    def get_positions(self):
        return self.pos

    def add_pos(self, x:int, y:int):
        self.pos.append([x,y])

    def get_name(self):
        return self.name

    def move(self, n:int):
        move_dir = self.determine_move_direction()
        for loc in self.pos:
            #loc[0] is x, loc[1] is y
            
            loc[0] = loc[0] + n * move_dir[0]
            loc[1] = loc[1] + n * move_dir[1]
            self.gas -= n
        #accept positive or negative
        #move base on move_dir... i.e down and left are negative, up and right are positve
        #if the head tile can move then so can the rest
        

    def is_vehicle_complete(self):
        #mainly for testing 
        #check that all positions are adjacent
        pass
    
    def __str__(self):
        #Create a vehicle to gas string. Do not output if gas is 100. i.e "C3 B4 H1"
        print(self.pos)

    def determine_move_direction(self):
        #vehicles need at least 2 entries
        if self.pos[0][0] == self.pos[1][0]: 
            #Can only move up/down
            return [0,1]
        else:
            #Can only move left right
            return [1,0]

