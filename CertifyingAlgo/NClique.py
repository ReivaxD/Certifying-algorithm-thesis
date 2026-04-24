
def cliqueNtoClause(edge, vertex, N):
    clauses = []
    varList = []
    counter = 1

    # On crée un tableau de variables classées par sommet 
    # (ex : Sommet A à le tableau [1, 2, 3, 4, 5] pour N = 5 et représente les 5 positions que peut avoir le sommet A)
    for v in range(vertex):
        var = []
        for w in range(N):
            var.append(counter)
            counter += 1
        varList.append(var)
    
    # On crée un tableau contenant les sommets pour une même position dans vartemp
    # (ex : Position 1 à le tableau [1, 6, 11, 16, 21] pour N = 5 et représente les 5 sommets que peut avoir la position 1)
    # Ce tableau correspond à la règle 2 : 
    # Chaque position dans la clique doit être attribuée à un sommet
    vartemp = []
    for v in range(N):
        var = []
        for w in range(vertex):
            var.append(varList[w][v])
        clauses.append(var)
        vartemp.append(var)

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

    # Similaires aux lignes 32-37 mais en utilisant le tableau des positions (vartemp) plutot que celui des sommets (valList)
    for l in vartemp:
        for x in l:
            for y in l:
                if ([-x , -y] not in clauses) and ([-y , -x] not in clauses) and (x != y):
                    clauses.append([-x, -y])

    # La règle 5 damande de créer des couples de variables lorsqu'on ne trouve pas d'arêtes dans le graphe 
    # on cherche donc les position dans le tableau edge qui sont égale à 0 (diagonale exclue)
    # on ajoute ensuite toute les combinaisons de variables liées aux deux sommets de cette arête
    # exemple : la valeur de l'arête X-Y = 0. Donc on crée une clause pour chaque positions possible ou les sommets X et Y sont tout les deux présents
    # supposons deux position possible la position 1 et 2. Alors les couples (non X1 ou non Y1) et (non X2 ou non Y1) et (non X1 ou non Y2) et (non X2 ou non Y2) seront crées
    for x in range(vertex):
        for y in range(vertex):
            if(edge[x][y] == 0) and (x != y):
                for a in range(N):
                    for b in range(N):
                        if ([-varList[x][a], -varList[y][b]] not in clauses) and ([-varList[x][b], -varList[y][a]] not in clauses):
                            clauses.append([-varList[x][a], -varList[y][b]])
    return clauses
