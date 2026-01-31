class CDCLSolver:
    def __init__(self, clauses):
        self.clauses = clauses[:]
        # Dictionnaire de variables avec leur valeur booleenne
        self.assignment = {}
        # La profondeur pour le backtracking
        self.level = {}
        # reason donne pour chaque variable x assignée dans le solveur :
        # None si littéral assigné par défaut
        # Sinon alors la valeur de reason est C, la clause ayant mené à l'assignation "forcée" (ie. Si tout les litéraux de C sont faux, alors x doit etre vrai)
        # Cette variable fait office de graphe d'implication
        self.reason = {}
        # Profondeur actuelle
        self.decision_level = 0

    def value(self, lit):
        var = abs(lit)
        if var not in self.assignment:
            return None
        val = self.assignment[var]
        return val if lit > 0 else not val

    # On applique la propagation
    def unit_propagation(self):
        changed = True
        # On continue la propagation tant qu'on a fait au moins un changement
        while changed:
            changed = False
            for clause in self.clauses:
                # Les littéraux vallent soit Vrai, soit Faux soit None (si pas encore assigné)
                values = [self.value(l) for l in clause]
                if all(v is False for v in values):
                    # conflit (Si tous faux)
                    return clause  
                if values.count(None) == 1 and all(v is False or v is None for v in values):
                    lit = clause[values.index(None)]
                    self.assign(lit, clause)
                    changed = True
        return None

    def assign(self, lit, reason=None):
        var = abs(lit)
        self.assignment[var] = (lit > 0)
        self.level[var] = self.decision_level
        self.reason[var] = reason

    # Pour choisir un littéral parmis celles non assignées
    def pick_branching_literal(self):
        for clause in self.clauses:
            for lit in clause:
                if abs(lit) not in self.assignment:
                    return lit
        return None

    # Traite les causes du conflit et la position pour revenir en arriere avec le backtracking
    def analyze_conflict(self, conflict_clause):
        learnt = conflict_clause[:]
        while True:
            # Crée une clause pour traiter le conflit
            current_level_lits = [
                l for l in learnt
                if self.level.get(abs(l), -1) == self.decision_level
            ]
            if len(current_level_lits) <= 1:
                break

            lit = current_level_lits[0]
            reason = self.reason.get(abs(lit))
            if reason is None:
                break
            # crée une liste avec 
            learnt = list(set(learnt + reason) - {lit, -lit})

        # Cherche la position pour le backtracking
        backjump = 0
        for lit in learnt:
            lvl = self.level.get(abs(lit), 0)
            if lvl != self.decision_level:
                backjump = max(backjump, lvl)

        return learnt, backjump

    # Pour faire le backtracking 
    def backjump(self, level):
        to_remove = [v for v in self.assignment if self.level[v] > level]
        # Revenir en arrière signifie enlever les étapes parcourues jusqu'à arriver à la profondeur souhaitée
        for v in to_remove:
            del self.assignment[v]
            del self.level[v]
            del self.reason[v]
        self.decision_level = level

    def solve(self):
        while True:
            # On applique la propagation unitaire
            conflict = self.unit_propagation()
            # Si il y a eu un conflit dans l'itération précédente, celle-ci est retournée
            if conflict:
                if self.decision_level == 0:
                    return False, None
                # Si on a trouvé un conflit, il va falloir le traiter (ajouter une clause et faire du backtracking)
                learnt, backjump = self.analyze_conflict(conflict)
                self.clauses.append(learnt)
                self.backjump(backjump)
                self.assign(learnt[0], learnt)
            else:
                # Si pas de propagation possible et pas de conflits
                lit = self.pick_branching_literal()
                if lit is None:
                    return True, self.assignment
                # Si on assigne une valeur de plus, ca correspond a descendre plus loin dans l'arbre de recherche
                self.decision_level += 1
                self.assign(lit)


clause1 = [[1, 2],[-1, 3],[-2, -3]] # ie. (x1 ∨ x2) ∧ (¬x1 ∨ x3) ∧ (¬x2 ∨ ¬x3)
clause2 = [[1, -4], [-1, 4], [1, -3, -8], [1, 8, 12], [2, 11], [-7, -3, 9], [-7, 8, -9], [7, 8, -10], [7, 10, -12]]
clause3 = [[1],[-1, 2],[-2, 3],[-3, 4],[-1, 5],[-5, 6],[-6, 7],[-4, -7]]  # Problème CNF sans solution

solver = CDCLSolver(clause2)
sat, model = solver.solve()

print("Résolvable ?" , sat)
print("Assignation possible :", model)
