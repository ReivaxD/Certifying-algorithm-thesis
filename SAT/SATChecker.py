def resolve(clauses, model):
    for clause in clauses:
        if not(checkClause(clause, model)):
            print("UNSAT")
            return False
    print("SAT")
    return True

def checkClause(clause, model):
    for l in clause:
        if l > 0:
            if model[l] == True:
                return True
        else:
            if model[abs(l)] == False:
                return True
    print("clause problematique :")
    print(clause)
    return False

clauses = [[1, -4], [-1, 4], [1, -3, -8], [1, 8, 12], [2, 11], [-7, -3, 9], [-7, 8, -9], [7, 8, -10], [7, 10, -12]]
modeltrue = {1: True, 4: True, 3: False, 8: False, 12: True, 7: True, 9: False, 2: True, 11: True, 10: False}
modelFalse = {1: False, 4: True, 3: False, 8: False, 12: False, 7: False, 9: False, 2: False, 11: False, 10: False}

print(resolve(clauses, modelFalse))