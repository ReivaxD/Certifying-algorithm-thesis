
def cliquetoClause(edge, vertex):
    clauses = []
    varList = []
    counter = 1
    for v in range(vertex):
        var = []
        for w in range(vertex):
            var.append(counter)
            counter += 1
        varList.append(var)
    
    vartemp = []
    for v in range(vertex):
        var = []
        for w in range(vertex):
            var.append(varList[w][v])
        clauses.append(var)
        vartemp.append(var)

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
        vartemp.append(var)

    for l in vartemp:
        for x in l:
            for y in l:
                if ([-x , -y] not in clauses) and ([-y , -x] not in clauses) and (x != y):
                    clauses.append([-x, -y])

    for x in range(vertex):
        for y in range(vertex):
            if(edge[x][y] == 0) and (x != y):
                for a in range(vertex):
                    for b in range(vertex):
                        if ([-varList[x][a], -varList[y][b]] not in clauses) and ([-varList[x][b], -varList[y][a]] not in clauses):
                            clauses.append([-varList[x][a], -varList[y][b]])
    return clauses



# exemple du mémoire :

# le format : le nombre de sommets
vertex = 3
# un tableau R x R contenant un 1 si deux sommets sont connectés (0 sinon)
edge = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
print(cliquetoClause(edge, vertex))