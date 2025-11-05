from pysat.solvers import Glucose3

# Création du solveur
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
is_sat = solver.solve()
print("SATISFIABLE ?" , is_sat)

if is_sat:
    model = solver.get_model()
    print("Modèle trouvé :", model)

print("-----------")
print("SATISFIABLE ?" , solver.solve(assumptions=[1,2,3,4,5,6,-7,8,9,10,11,12]))