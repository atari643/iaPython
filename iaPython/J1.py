import game as g

def J1():
    statueL = False;
    statueC = False
    while(statueL==False & statueC==False):
        ligne=int(input("Choisi la ligne où tu veux placer ton rond (O): "))
        statueL=check(ligne);
        colonne=int(input("Choisi la colonne où tu veux placer ton rond (O): "))
        statueC = check(colonne);
    g.tab[ligne][colonne]=1;
    print(g.plateau())
    
def check(nombre):
    if(type(nombre)==int):
        if(nombre>=0 & nombre<len(g.tab)):
            return True
        else:
            return False
    else:
        return False
J1()