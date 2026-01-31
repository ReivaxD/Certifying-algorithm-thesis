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

    # Retourne la valeur logique de ce littéral avec les assignations actuelles
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
                # Si exactement 1 littéral est non assigné et tout les autres sont Faux
                if values.count(None) == 1 and all(v is False or v is None for v in values):
                    lit = clause[values.index(None)]
                    # On assigne cette variable et on réittère la propagation unitaire (car l'assignation peut créer d'autre assignation par implication) 
                    self.assign(lit, clause)
                    changed = True
        return None

    # On assigne une variable
    def assign(self, lit, reason=None):
        # Quel est le littéral à assigner
        var = abs(lit)
        # On assigne la variable (exemple : Si elle doit etre fausse, alors toutes les valeurs de la clause impliquée seront fausses et la valeur du littéral est négative (ie. -x1))
        self.assignment[var] = (lit > 0)
        # On avance dans la profondeur
        self.level[var] = self.decision_level
        # On ajoute None si on provient de l'assignation par défaut
        # Sinon, on ajoute la clause responsable de l'assignation 
        self.reason[var] = reason

    # Pour choisir un littéral parmis ceux non assignés
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
            # Combien de littéraux de la clause viennent du niveau de décision courant
            current_level_lits = [
                l for l in learnt
                if self.level.get(abs(l), -1) == self.decision_level
            ]
            # La clause est (supposée) assertive (1 seul littéral -> on sait qu'on doit ajouter une clause et faire du backtracking)
            if len(current_level_lits) <= 1:
                break

            # On remonte au littéral de base pour savoir la cause de la présence 
            lit = current_level_lits[0]
            reason = self.reason.get(abs(lit))
            # On ne peut pas remonter plus loin
            if reason is None:
                break
            # Si aucun des sénarios précédents on combine la clause courante avec la clause reason
            learnt = list(set(learnt + reason) - {lit, -lit})

        # Cherche la position pour le backtracking
        backjump = 0
        for lit in learnt:
            lvl = self.level.get(abs(lit), 0)
            if lvl != self.decision_level:
                # le niveau où la clause apprise deviendra unitaire (la dernière)
                backjump = max(backjump, lvl)

        return learnt, backjump

    # Pour faire le backtracking 
    def backjump(self, level):
        to_remove = [v for v in self.assignment if self.level[v] > level]
        # Revenir en arrière signifie enlever les étapes parcourues jusqu'à arriver à la profondeur souhaitée
        for v in to_remove:
            # Raisonnement similaire à la méthode assign() mais avec suppression plutot qu'ajout
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
