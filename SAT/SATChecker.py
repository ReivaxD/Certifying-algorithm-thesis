from pysat.solvers import Glucose3

def resolveSAT(clauses, model):
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

def resolveUNSAT(clauses):
    with Glucose3(with_proof=True) as solver:
        for clause in clauses:
            solver.add_clause(clause)

        sat = solver.solve()
        if not sat:
            print("UNSAT")
            proof = solver.get_proof()
            print("Preuve (DRAT) :")
            print(proof)
            for step in proof:
                print(step)
        else:
            print("SAT")

clause1 = [[1, 2],[-1, 3],[-2, -3]] # ie. (x1 ∨ x2) ∧ (¬x1 ∨ x3) ∧ (¬x2 ∨ ¬x3)
clause2 = [[1, -4], [-1, 4], [1, -3, -8], [1, 8, 12], [2, 11], [-7, -3, 9], [-7, 8, -9], [7, 8, -10], [7, 10, -12]]
clause3 = [[1],[-1, 2],[-2, 3],[-3, 4],[-1, 5],[-5, 6],[-6, 7],[-4, -7]]  # Problème CNF sans solution

# Models a tester pour la clause 2
modeltrue = {1: True, 4: True, 3: False, 8: False, 12: True, 7: True, 9: False, 2: True, 11: True, 10: False}
modelFalse = {1: False, 4: True, 3: False, 8: False, 12: False, 7: False, 9: False, 2: False, 11: False, 10: False}

print(resolveSAT(clause3, modelFalse))

# Le résultat de resolvaUNSAT(clause3) est donné dans DRATproof.txt