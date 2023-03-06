# videoGame.py
# IS4010-002 Spring 2023

import random
def play():
    '''
    returns True if you won, False if you lost 
    '''
    if random.randint(0,100) == 10:
        raise Exception("Game Crashed")
    return random.choice([True, False])