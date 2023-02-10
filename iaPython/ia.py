import game as g
import numpy as np
import random as rd
Qvaleur=[[]]

alpha = 0.1
gamma = 0.9 
epsilon = 0.1
def jeu():
    s=g.tab
    while(etat_final==False):
        etatSuivant = action(s)
        
        
        
        
        

def etat_final(etat):
    assert(etat==np.ndarray)
    for i in etat:
        if(i==0):
            return False
    return True

def action(etat):
    valeur = 0
    tab = actionPossible(etat)
    if(epsilon<rd.randint(0, 1)):
        valeur = rd.randint(0, len(tab))
    etat[valeur][0, 1]=2
    return etat

def actionPossible(etat):
    tab = []
    for i in range(len(etat)):
        for j in range(len(etat[0])):
            if(etat[i][j]==0):
                tab.append([i, j])
    return tab

def recompence(etat):
    