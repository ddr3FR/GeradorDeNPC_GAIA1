import random

def qts_energi(pts_PDA):
    contador = 0
    total_PE = 0
    if pts_PDA == 1:
        total_PE = 5
    elif pts_PDA > 1: 
        while pts_PDA > 0:
            contador += 1
            pts_PDA -=1
    
    total_PE = 5 + contador
    return total_PE

def qts_life(pts_PDA, pts_vigor):
    vidaInical = 30
    vidaMax = 0
    lifeVlrVL = 0
    if pts_PDA == 1:
        vidaMax = vidaInical + random.randint(1,6) + pts_vigor
    elif pts_PDA > 1:
        while pts_PDA > 0:
            lifeVlrVL += random.randint(1,6)
            pts_PDA -=1
        vidaMax = vidaInical + lifeVlrVL + pts_vigor
    return vidaMax





