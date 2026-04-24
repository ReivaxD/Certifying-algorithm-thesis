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

def resolveUNSAT(clauses, name):
    with Glucose3(with_proof=True) as solver:
        for clause in clauses:
            solver.add_clause(clause)

        sat = solver.solve()
        if not sat:
            print("UNSAT")
            proof = solver.get_proof()
            with open(name + ".txt", "w") as f:
                for step in proof:
                    f.write(step)
                    f.write("\n")
        else:
            print("SAT")
    return sat
