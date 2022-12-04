
from random import seed
import random

# seed random number generator
seed(1)


EXIT_ROW = 2
AMBO = 'A'
VEHICLES = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
MIN_LEN = 2
MAX_LEN = 4
SIZE = 6

for i in range(0, 50):
    vehicles = {}
    num_vehicles = random.randint(2, len(VEHICLES))
    v_gas = {}
    #generate ambo position
  
    ambo_start_pos = random.randint(13, 17)
    if ambo_start_pos == 13:
        ambo_second_pos = 14
    elif ambo_start_pos == 18:
        ambo_second_pos = 17
    else:
        ambo_second_pos = ambo_start_pos + 1
    vehicles[ambo_start_pos] = 'A'
    vehicles[ambo_second_pos] = 'A'
    v_gas['A'] = random.randint(0, 100)
    for j in range(0, num_vehicles):
        cur_vehicle = VEHICLES[j]
        
        attemps = 0
        while attemps < 8:
            cur_positions = []
            start_pos = random.randint(0, 35)
        
            if start_pos in vehicles.keys():
                continue
            
            cur_positions.append(start_pos)
            size = random.randint(MIN_LEN, MAX_LEN)
            if random.random() < 0.5:
                next_pos = 6
                for s in range(0, size -1):
                    pos = start_pos + (next_pos * (s +1))
                    if pos > 35:
                        next_pos *= -1
                        pos = start_pos + (next_pos * (s +1))
                    
                    cur_positions.append(pos)

            else:
                next_pos = 1
                for s in range(0, size-1 ):
                    pos = start_pos + (next_pos * (s +1))
                    if pos > 35 or (pos + 1) % 6 == 0 or pos < 0:
                        next_pos *= -1
                        pos = start_pos + (next_pos * (s +1))

                    
                    cur_positions.append(pos)
            s1 = set(cur_positions)
            s2 = set(vehicles.keys())
            if s1.intersection(s2):
                attemps += 1
            else:
                break
        s1 = set(cur_positions)
        s2 = set(vehicles.keys())
        if len(cur_positions) > MAX_LEN:
            pass
        if not s1.intersection(s2) and  len(s1) >= MIN_LEN:
            for p in cur_positions:
                vehicles[p] = cur_vehicle
                v_gas[cur_vehicle] = random.randint(0, 100)
        else:
            pass
    str_ = ''
    for p in range(0, 36):        
        if p in vehicles.keys():
            str_ += vehicles[p]
        else:
            str_ += '.'
    for v,g in v_gas.items():
        if g != 100:
            str_ += ' {}{}'.format(v,g)
    print(str_)
        