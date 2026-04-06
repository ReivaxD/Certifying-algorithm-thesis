def hamiltontoClause(edge, vertex):
    clauses = []
    counter = 1
    for v in range(vertex):
        var = []
        for w in range(vertex):
            var.append(counter)
            counter += 1
        clauses.append(var)

    varList = clauses.copy()
    for l in varList:
        for x in l:
            for y in l:
                if ([-x , -y] not in clauses) and ([-y , -x] not in clauses) and (x != y):
                    clauses.append([-x, -y])

    vartemp = []
    for v in range(vertex):
        var = []
        for w in range(vertex):
            var.append(varList[w][v])
        clauses.append(var)
        vartemp.append(var)

    for l in vartemp:
        for x in l:
            for y in l:
                if ([-x , -y] not in clauses) and ([-y , -x] not in clauses) and (x != y):
                    clauses.append([-x, -y])
        
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

# exemple du mémoire :

# le format : le nombre de sommets
vertex = 5
# un tableau R x R contenant un 1 si deux sommets sont connectés (0 sinon)
edge = [[0, 1, 1, 0, 1], [1, 0, 1, 0, 0], [1, 1, 0, 1, 1], [0, 0, 1, 0, 1], [1, 0, 1, 1, 0]]

print(hamiltontoClause(edge, vertex))
