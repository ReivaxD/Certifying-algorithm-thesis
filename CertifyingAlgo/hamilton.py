
def hamiltontoClause(edge, vertex):

    clauses = []
    counter = 1
    # Soit R = le nombre de sommets (vertex)
    # On crée l'ensemble de variables R x R
    # En meme temps que d'appliquer la première règle :
    # Il faut que chaque sommet ait une position attribuée
    for v in range(vertex):
        var = []
        for w in range(vertex):
            var.append(counter)
            counter += 1
        clauses.append(var)

    # On sauvegarde les variables classées par sommet 
    # (ex : Sommet A à le tableau [1, 2, 3, 4, 5] pour R = 5 et représente les 5 positions que peut avoir le sommet A)
    varList = clauses.copy()

    # Un même sommet ne peut pas avoir deux positions différentes
    # On regarde chaque liste présente dans varList
    # chacune de ses listes possèdent R éléments et représentent les différentes positions d'un même sommet
    # il ne peut pas exister une paire avec la valeur "vrai"
    for l in varList:
        for x in l:
            for y in l:
                # On elimine les valeurs redondantes et on evite de regarder la diagonale du tableau edge 
                if ([-x , -y] not in clauses) and ([-y , -x] not in clauses) and (x != y):
                    clauses.append([-x, -y])

    # Règle 3 : Une même position ne peut pas être attribuée à deux sommets différents
    vartemp = []
    for v in range(vertex):
        var = []
        for w in range(vertex):
            # On crée un ensemble avec les éléments de valList colonne par colonne
            var.append(varList[w][v])
        clauses.append(var)
        # On sauvegarde les sommets pour une même position dans vartemp
        # (ex : Position 1 à le tableau [1, 6, 11, 16, 21] pour R = 5 et représente les 5 sommets que peut avoir la position 1)
        vartemp.append(var)

    # Similaires aux lignes 25-30 mais en utilisant le tableau des positions (vartemp) plutot que celui des sommets (valList)
    for l in vartemp:
        for x in l:
            for y in l:
                if ([-x , -y] not in clauses) and ([-y , -x] not in clauses) and (x != y):
                    clauses.append([-x, -y])
        
    # pour chaque arête manquante (= position dans le tableau edge ou on a un 0) 
    # (en excluant la diagonale)
    # pour une arête manquante X-Y
    # on empèche les position se suivant (a et a+1)
    # on crée une dernière position bloquée pour la position en tête de cycle et en fin de cycle
    # on répète le processus pour l'arête Y-X (car sens du chemin important pour problème cycle hamiltonien)
    for x in range(vertex):
        for y in range(vertex):
            if(edge[x][y] == 0) and (x != y):
                    for a in range(vertex-1):
                        clauses.append([-varList[x][a], -varList[y][a+1]])
                    clauses.append([-varList[x][vertex-1], -varList[y][0]])
                    for b in range(vertex-1):
                        clauses.append([-varList[y][b], -varList[x][b+1]])
                    clauses.append([-varList[y][vertex-1], -varList[x][0]])

    return clauses
