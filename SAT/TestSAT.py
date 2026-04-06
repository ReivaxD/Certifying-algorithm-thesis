from pysat.solvers import Glucose3

# Création du solveur

clauseList = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [-1, -2], [-1, -3], [-1, -4], [-1, -5], [-2, -3], [-2, -4], [-2, -5], [-3, -4], [-3, -5], [-4, -5], [-6, -7], [-6, -8], [-6, -9], [-6, -10], [-7, -8], [-7, -9], [-7, -10], [-8, -9], [-8, -10], [-9, -10], [-11, -12], [-11, -13], [-11, -14], [-11, -15], [-12, -13], [-12, -14], [-12, -15], [-13, -14], [-13, -15], [-14, -15], [-16, -17], [-16, -18], [-16, -19], [-16, -20], [-17, -18], [-17, -19], [-17, -20], [-18, -19], [-18, -20], [-19, -20], [-21, -22], [-21, -23], [-21, -24], [-21, -25], [-22, -23], [-22, -24], [-22, -25], [-23, -24], [-23, -25], [-24, -25], [1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5], [6, 7], [6, 8], [6, 9], [6, 10], [7, 8], [7, 9], [7, 10], [8, 9], [8, 10], [9, 10], [11, 12], [11, 13], [11, 14], [11, 15], [12, 13], [12, 14], [12, 15], [13, 14], [13, 15], [14, 15], [16, 17], [16, 18], [16, 19], [16, 20], [17, 18], [17, 19], [17, 20], [18, 19], [18, 20], [19, 20], [21, 22], [21, 23], [21, 24], [21, 25], [22, 23], [22, 24], [22, 25], [23, 24], [23, 25], [24, 25], [1, 6, 11, 16, 21], [2, 7, 12, 17, 22], [3, 8, 13, 18, 23], [4, 9, 14, 19, 24], [5, 10, 15, 20, 25], [-1, -6], [-1, -11], [-1, -16], [-1, -21], [-6, -11], [-6, -16], [-6, -21], [-11, -16], [-11, -21], [-16, -21], [-2, -7], [-2, -12], [-2, -17], [-2, -22], [-7, -12], [-7, -17], [-7, -22], [-12, -17], [-12, -22], [-17, -22], [-3, -8], [-3, -13], [-3, -18], [-3, -23], [-8, -13], [-8, -18], [-8, -23], [-13, -18], [-13, -23], [-18, -23], [-4, -9], [-4, -14], [-4, -19], [-4, -24], [-9, -14], [-9, -19], [-9, -24], [-14, -19], [-14, -24], [-19, -24], [-5, -10], [-5, -15], [-5, -20], [-5, -25], [-10, -15], [-10, -20], [-10, -25], [-15, -20], [-15, -25], [-20, -25], [-1, -17], [-2, -18], [-3, -19], [-4, -20], [-5, -16], [-16, -2], [-17, -3], [-18, -4], [-19, -5], [-20, -1], [-6, -17], [-7, -18], [-8, -19], [-9, -20], [-10, -16], [-16, -7], [-17, -8], [-18, -9], [-19, -10], [-20, -6], [-6, -22], [-7, -23], [-8, -24], [-9, -25], [-10, -21], [-21, -7], [-22, -8], [-23, -9], [-24, -10], [-25, -6], [-16, -2], [-17, -3], [-18, -4], [-19, -5], [-20, -1], [-1, -17], [-2, -18], [-3, -19], [-4, -20], [-5, -16], [-16, -7], [-17, -8], [-18, -9], [-19, -10], [-20, -6], [-6, -17], [-7, -18], [-8, -19], [-9, -20], [-10, -16], [-21, -7], [-22, -8], [-23, -9], [-24, -10], [-25, -6], [-6, -22], [-7, -23], [-8, -24], [-9, -25], [-10, -21]]

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

solver = Glucose3()
# Clause :
for clause in clauseList:
    solver.add_clause(clause)

is_sat = solver.solve()
# Vérifie si c’est satisfaisable
print("SATISFIABLE ?" , is_sat)

if is_sat:
    model = solver.get_model()
    print("Modèle trouvé :", model)


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