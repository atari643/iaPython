import matplotlib as plt
import numpy as np

tab=np.array([[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]])
def plateau():
    print(type(tab))
    plateau = "";
    for i in range(len(tab)):
        plateau+="|"
        for y in range(len(tab[0])):
            if(tab[i][y]==0):
                plateau+="   |"
            if(tab[i][y]==1):
                plateau+=" O |"
            if(tab[i][y]==2):
                plateau+=" X |"
        plateau+="\n"
    return plateau
print(plateau())