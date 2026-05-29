class CDCLSolver:
    def __init__(self, clauses):
        self.clauses = clauses[:]
        self.assignment = {}
        self.level = {}
        self.reason = {}
        self.decision_level = 0

    def value(self, lit):
        var = abs(lit)
        if var not in self.assignment:
            return None
        val = self.assignment[var]
        return val if lit > 0 else not val

    def unit_propagation(self):
        changed = True
        while changed:
            changed = False
            for clause in self.clauses:
                values = [self.value(l) for l in clause]
                if any(v is True for v in values):
                    continue  # clause déjà satisfaite, on ignore
                if all(v is False for v in values):
                    return clause
                if values.count(None) == 1 and all(v is False or v is None for v in values):
                    lit = clause[values.index(None)]
                    self.assign(lit, clause)
                    changed = True
        return None

    def assign(self, lit, reason=None):
        var = abs(lit)
        if var in self.assignment:  # déjà assigné, on ne touche pas
            return
        self.assignment[var] = (lit > 0)
        self.level[var] = self.decision_level
        self.reason[var] = reason

    def pick_branching_literal(self):
        for clause in self.clauses:
            for lit in clause:
                if abs(lit) not in self.assignment:
                    return lit
        return None

    def analyze_conflict(self, conflict_clause):
        learnt = set(conflict_clause)

        while True:
            current_level_lits = [
                l for l in learnt
                if self.level.get(abs(l), -1) == self.decision_level
            ]

            if len(current_level_lits) <= 1:
                break

            # Parmi les littéraux du niveau courant ayant une reason,
            # on prend le plus récemment assigné
            candidates = [
                l for l in current_level_lits
                if self.reason.get(abs(l)) is not None
            ]

            if not candidates:
                break

            pivot = max(
                candidates,
                key=lambda l: list(self.assignment.keys()).index(abs(l))
            )

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

        # Niveau de backjump = 2ème niveau le plus haut (hors littéral assertif)
        backjump = 0
        for lit in learnt[1:]:
            lvl = self.level.get(abs(lit), 0)
            backjump = max(backjump, lvl)

        return learnt, backjump

    def backjump(self, level):
        to_remove = [v for v in self.assignment if self.level[v] > level]
        for v in to_remove:
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

            lit = self.pick_branching_literal()
            if lit is None:
                return True, self.assignment

            self.decision_level += 1
            self.assign(lit)

            inner = 0
            while True:
                inner += 1
                if inner > 10000:

                    return False, None

                conflict = self.unit_propagation()
                if conflict is None:
                    break

                if self.decision_level == 0:
                    return False, None

                learnt, backjump_level = self.analyze_conflict(conflict)
                

                if not learnt:
                    return False, None

                self.clauses.append(learnt)
                self.backjump(backjump_level)
                self.assign(learnt[0], learnt)