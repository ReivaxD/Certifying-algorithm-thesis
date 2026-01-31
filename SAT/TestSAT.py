from pysat.solvers import Glucose3

# Création du solveur

clauseList = [[1, 4], [1, -3, -8], [1, 8, 12], [2, 11], [-7, -3, 9], [-7, 8, -9], [7, 8, -10], [7, 10, -12]]

def CDCL(clauseList):
    
    solver = Glucose3()
    for clause in clauseList:
        solver.add_clause(clause)
    
    # Récupère les sommets et arêtes du graphe d'implication de la liste de clauses
    edge, vector = ImplicationGraph(clauseList)

    # On génère un dictionnaire avec les sommets présents dans ClauseList
    dictVar = {}
    for i in edge:
        dictVar[i] = False
        dictVar[-i] = False

    while True:
        # On applique la propagation unitaire
        dictVar = propagation(dictVar, vector)

        if(True):
            return True


def CDCLTest(clauseList, vectorList, edgeList):

    solver = Glucose3()

    for clause in clauseList:
        solver.add_clause(clause)

    dictVar = {}
    for i in edgeList:
        dictVar[i] = False
        dictVar[-i] = False

    dictVar[edgeList[0]] = True
    NewdictVar = propagation(dictVar, vectorList)
    dictVar = NewdictVar
    for i in edgeList:
        while (NewdictVar != dictVar):
            NewdictVar = propagation(dictVar, vectorList)
            print(solver.propagate(toList(NewdictVar)))
        dictVar[i] = True
        print(NewdictVar)
        print(dictVar)

def toList(varDict):
    l = []
    for key in varDict:
        if(varDict[key]):
            l.append(key)
    return l


def propagation(dictVar, vectorList):
    for vector in vectorList:
        if(isinstance(vector[0], int)):
            if(dictVar[vector[0]]):
                dictVar[vector[1]] = True
        else:
            if((dictVar[vector[0][0]])) and ((dictVar[vector[0][1]])):
                dictVar[vector[1]] = True
    return dictVar

def ImplicationGraph(ClauseList):
    edgeList = []
    vectorList = []

    for clause in ClauseList:
        for number in clause:
            if(number not in edgeList) and (-number not in edgeList):
                edgeList.append(number)
                edgeList.append(-number)
    
    edgeList.sort()

    for clause in ClauseList:
        if(len(clause) == 2):
            vectorList.append((-clause[1], clause[0]))
            vectorList.append((-clause[0], clause[1]))

        if(len(clause) == 3):
            vectorList.append(([-clause[0], -clause[1]], clause[2]))
            vectorList.append(([-clause[1], -clause[2]], clause[0]))
            vectorList.append(([-clause[0], -clause[2]], clause[1]))

    return edgeList, vectorList
"""
solver = Glucose3()
# Clause :
solver.add_clause([1, 4])
solver.add_clause([1, -3, -8])
solver.add_clause([1, 8, 12])
solver.add_clause([2, 11])
solver.add_clause([-7, -3, 9])
solver.add_clause([-7, 8, -9])
solver.add_clause([7, 8, -10])
solver.add_clause([7, 10, -12])

# Vérifie si c’est satisfaisable
print("SATISFIABLE ?" , is_sat)

if is_sat:
    model = solver.get_model()
    print("Modèle trouvé :", model)

print("-----------")
print("SATISFIABLE ?" , solver.solve(assumptions=[1,2,3,4,5,6,-7,8,9,10,11,12]))

for model in solver.enum_models():
    print(model)

print(solver.propagate([-1, -4]))
"""
edge, vector = ImplicationGraph(clauseList)
#print(edge)
#print(vector)

#CDCL(clauseList, vector, edge)
'''
solver = Glucose3()

for clause in clauseList:
    solver.add_clause(clause)

dictVar = {}
for i in edge:
    dictVar[i] = False
    dictVar[-i] = False
dictVar[-1] = True
dictVar[3] = True

print(vector)
print(propagation(dictVar, vector))
'''