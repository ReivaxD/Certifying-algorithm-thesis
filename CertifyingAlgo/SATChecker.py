from pysat.solvers import Glucose3
from pysat.formula import CNF
import subprocess
import tempfile
import os

# Vérifie si un modèle est solution d'un problème SAT
def resolveSAT(clauses, model):
    for clause in clauses:
        if not(checkClause(clause, model)):
            #print("UNSAT")
            return False
    #print("SAT")
    return True

# Vérifie si une clause est vraie ou fausse
def checkClause(clause, model):
    for l in clause:
        if l > 0:
            if model[l] == True:
                return True
        else:
            if model[abs(l)] == False:
                return True
    #print("clause problematique :")
    #print(clause)
    return False

# Génrère une preuve UNSAT et la vérifie avec drat-trim
def resolveUNSAT(clauses, name=None, timeout=60, tmp_dir="/dev/shm"):
    with tempfile.TemporaryDirectory(dir=tmp_dir) as td:
        cnf_path = os.path.join(td, "problem.cnf")
        drat_path = os.path.join(td, "proof.drat")

        CNF(from_clauses=clauses).to_file(cnf_path)

        with Glucose3(bootstrap_with=clauses, with_proof=True) as solver:
            sat = solver.solve()
            if sat:
                print("SAT (incohérence)")
                return None
            proof = solver.get_proof()

        # On sauvegarde la preuve produite par le solveur
        with open(drat_path, "w") as f:
            for step in proof:
                f.write(step + "\n")

        # On utilise drat-trim pour vérifier le certificat
        result = subprocess.run(
            ["drat-trim", cnf_path, drat_path, "-t", str(timeout)],
            capture_output=True, text=True, timeout=timeout + 5
        )
        verified = "s VERIFIED" in result.stdout
        #print("UNSAT verifiée" if verified else "UNSAT NON verifiée")
        return verified