class CDCLSolver:
    def __init__(self, clauses):
        self.clauses = clauses[:]
        # Dictionnaire de variables avec leur valeur booleenne
        self.assignment = {}
        # La profondeur pour le backtracking
        self.level = {}
        # raison donne pour chaque variable x assignée dans le solveur :
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
                if any(v is True for v in values):
                    continue  # clause déjà satisfaite, on ignore
                # conflit (Si tous faux)
                if all(v is False for v in values):
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
        if var in self.assignment:  # déjà assigné, on ne touche pas
            return
    
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

    # On fusionne itérativement la clause courante avec la clause "reason" du littéral responsable du conflit
    # en éliminant ce littéral (le pivot). 
    # On s'arrête quand la clause est dite "assertive" : elle ne contient plus qu'un seul littéral du niveau
    # de décision courant, ce qui garantit qu'après backjump ce littéral sera propagé immédiatement par la propagation unitaire.
    def analyze_conflict(self, conflict_clause):

        # Mémorise les pivots déjà utilisés pour éviter de résoudre deux fois
        # sur la même variable, ce qui causerait un cycle infini.
        learnt = set(conflict_clause)

        while True:
            # Littéraux de la clause courante assignés au niveau de décision actuel.
            # Ce sont les seuls candidats au rôle de pivot.
            current_level_lits = [
                l for l in learnt
                if self.level.get(abs(l), -1) == self.decision_level
            ]

            # Condition d'arrêt : clause assertive.
            # Un seul littéral du niveau courant implique qu'après backjump, ce littéral
            # sera l'unique littéral non assigné de la clause et sera propagé.
            if len(current_level_lits) <= 1:
                break

            # Parmi les littéraux du niveau courant ayant une reason,
            # on prend le plus récemment assigné
            candidates = [
                l for l in current_level_lits
                if self.reason.get(abs(l)) is not None
            ]

            # Aucun candidat exploitable implique qu'on ne peut pas réduire davantage.
            if not candidates:
                break

            # Sélection du pivot : littéral du niveau courant le plus récemment
            # assigné (ordre chronologique inverse), avec une reason connue.
            # L'ordre chronologique inverse garantit la convergence : on "défait"
            # les implications dans l'ordre inverse de leur création.
            pivot = max(
                candidates,
                key=lambda l: list(self.assignment.keys()).index(abs(l))
            )

            # Étape de résolution :
            # learnt  = (learnt ∪ reason(pivot)) \ {pivot, ¬pivot}
            # On fusionne les deux clauses et on supprime le pivot des deux côtés
            # (littéral positif et négatif) pour l'éliminer proprement.
            reason = self.reason[abs(pivot)]
            learnt = (learnt | set(reason)) - {pivot, -pivot}

        learnt = list(learnt)

        # Identifier le littéral assertif : celui du niveau courant
        # C'est lui qui sera propagé après le backjump
        assertive = next(
            (l for l in learnt
             if self.level.get(abs(l), -1) == self.decision_level),
            None
        )

        # Le placer en position 0 pour que solve() le retrouve facilement
        if assertive is not None:
            learnt.remove(assertive)
            learnt = [assertive] + learnt

        # Calcul du niveau de backjump : on cherche le niveau le plus élevé
        # parmi les littéraux de la clause apprise qui ne sont PAS du niveau
        # courant. C'est le niveau auquel la clause deviendra unitaire
        # (un seul littéral non assigné) et déclenchera une propagation.
        backjump = 0
        for lit in learnt[1:]:
            lvl = self.level.get(abs(lit), 0)
            backjump = max(backjump, lvl)

        return learnt, backjump

    # Pour faire le backtracking 
    def backjump(self, level):

        # Revenir en arrière signifie enlever les étapes parcourues jusqu'à arriver à la profondeur souhaitée
        to_remove = [v for v in self.assignment if self.level[v] > level]
        for v in to_remove:
            # Raisonnement similaire à la méthode assign() mais avec suppression plutot qu'ajout
            del self.assignment[v]
            del self.level[v]
            del self.reason[v]
        self.decision_level = level

    def solve(self):
        conflict = self.unit_propagation()
        if conflict:
            return False, None

        outer = 0
        while True:
            outer += 1
            if outer > 10000:
                print("BOUCLE EXTERNE INFINIE")
                return False, None

            # Si pas de propagation possible et pas de conflits
            lit = self.pick_branching_literal()
            if lit is None:
                return True, self.assignment

            # Si on assigne une valeur de plus, ca correspond a descendre plus loin dans l'arbre de recherche
            self.decision_level += 1
            self.assign(lit)

            inner = 0
            while True:
                inner += 1
                if inner > 10000:

                    return False, None

                # On applique la propagation unitaire
                conflict = self.unit_propagation()
                # Si il y a eu un conflit dans l'itération précédente, celle-ci est retournée
                if conflict is None:
                    break

                if self.decision_level == 0:
                    return False, None

                # Si on a trouvé un conflit, il va falloir le traiter (ajouter une clause et faire du backtracking)
                learnt, backjump_level = self.analyze_conflict(conflict)
                

                if not learnt:
                    return False, None

                self.clauses.append(learnt)
                self.backjump(backjump_level)
                self.assign(learnt[0], learnt)