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


    def move_dir_to_str(self, n):
        move_dir = self.determine_move_direction()
        if n > 0 and move_dir[0]==1:
            return 'down'
        elif n < 0 and move_dir[0]==1:
            return 'up'
        elif n > 0 and move_dir[1]==1:
            return 'right'
        else:
            return 'left'

    def get_pos_list_if_moved(self, n:int):
        move_dir = self.determine_move_direction()
        new_positions = []
        for loc in self.pos:
            #loc[0] is x, loc[1] is y
            new_pos = []
            new_pos.append(loc[0] + n * move_dir[0])
            new_pos.append(loc[1] + n * move_dir[1])
            new_positions.append(new_pos)
        return new_positions

    def move(self, n:int):
        self.pos = self.get_pos_list_if_moved(n)
        self.gas -= abs(n)  

    
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

