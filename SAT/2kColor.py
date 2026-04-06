
def color2ktoClause(edge, vertex):
    clauses = []

    clause = []
    # on crée 2N variables avec N = nombre de sommets
    # on va lier chaque couple de variables deux a deux (i.e. il faut que chaque sommet aie une couleur attribuée)
    # exemple le premier sommet donne deux variables 1 et 2 et la clause [1, 2]
    for v in range(2*vertex):
        x = v+1
        clause.append(x)
        if(x%2 == 0):
            clauses.append(clause)
            clause = []
    
    # copie des variables groupées
    # la condition if élimine les doublons ("deux aretes" existent connectant les sommets A et B : AB et BA)
    # on ajoute les couple qui ne peuvent pas avoir la meme couleur pour une arête AB : [non A1 ou non B1] et [non A2 ou non B2]
    var = clauses
    for x in range(vertex):
            for y in range(vertex):
                 if(edge[x][y] == 1):
                        if [-var[y][0], -var[x][0]] not in clauses:
                            clauses.append([-var[x][0], -var[y][0]])
                        if [-var[y][1], -var[x][1]] not in clauses:
                            clauses.append([-var[x][1], -var[y][1]])

    return clauses

# exemple du mémoire :

# le format : le nombre de sommets
vertex = 3
# un tableau R x R contenant un 1 si deux sommets sont connectés (0 sinon)
edge = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]

print(color2ktoClause(edge, vertex))