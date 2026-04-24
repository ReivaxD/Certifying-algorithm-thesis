
def colorNktoClause(edge, vertex, N):
    clauses = []

    clause = []
    # on crée K*N variables avec K = nombre de sommets et N = nombre de couleur
    # on va lier chaque couple de variables deux a deux (i.e. il faut que chaque sommet aie une couleur attribuée)
    # exemple le premier sommet donne deux variables 1 et 2 et la clause [1, 2]
    i = 1
    for v in range(vertex):
        for w in range(N):
            clause.append(i)
            i += 1
        clauses.append(clause)
        clause = []

    # Sauvegarde du tableau des couleurs possibles par sommets
    var = clauses.copy()

    # Un même sommet ne peut avoir qu'une seule couleur.
    for v in range(vertex):
        for w in range(N):
            for x in range(w+1, N):
                clauses.append([-var[v][w], -var[v][x]])

    # copie des variables groupées
    # la condition if élimine les doublons ("deux aretes" existent connectant les sommets A et B : AB et BA)
    # on ajoute les couple qui ne peuvent pas avoir la meme couleur pour une arête AB : [non A1 ou non B1] et [non A2 ou non B2]
    for x in range(vertex):
            for y in range(x+1, vertex):
                 if(edge[x][y] == 1) and (x != y):
                        for i in range(N):
                            if [-var[y][i], -var[x][i]] not in clauses:
                                clauses.append([-var[x][i], -var[y][i]])

    return clauses
