import random

def sort_pda(nvl_dpa):

    if nvl_dpa == "n":
        esc_nvl = random.randint(1,3)
    if nvl_dpa == "a":
        esc_nvl = random.randint(4,9)
    if nvl_dpa == "h":
        esc_nvl = random.randint(10,20)
    if nvl_dpa == "l":
        esc_nvl = random.randint(21,25)
    if nvl_dpa == "s":
        esc_nvl = random.randint(26,30)
    if nvl_dpa == "t":
        esc_nvl = random.randint(1,30)
    
    return esc_nvl

    




