import networkx as nx
import time

countSAT = 0
countUNSAT = 0

# Le K pour K-coloring
K = 2
name = "graph9.g6"


def is_k_colorable(G: nx.Graph, k: int) -> bool:
    if k >= G.number_of_nodes():
        return True

    nodes = list(G.nodes())
    coloring = {}

    def backtrack(idx):
        if idx == len(nodes):
            return True
        node = nodes[idx]
        used = {coloring[nb] for nb in G.neighbors(node) if nb in coloring}
        for color in range(k):
            if color not in used:
                coloring[node] = color
                if backtrack(idx + 1):
                    return True
                del coloring[node]
        return False

    return backtrack(0)


with open("ressources/" + name, "r", encoding="utf-8") as f:
    nb_lignes = sum(1 for _ in f)

count = 0
start = time.time()

with open("ressources/" + name, "r", encoding="utf-8") as f:
    for ligne in f:
        G = nx.from_graph6_bytes(ligne.strip().encode())

        if is_k_colorable(G, K):
            countSAT += 1
        else:
            countUNSAT += 1

        count += 1
        if nb_lignes > 1000 and count % (nb_lignes // 10) == 0:
            print(f"{count}/{nb_lignes}")

end = time.time()

print(f"Nombre de problèmes SAT  : {countSAT}")
print(f"Nombre de problèmes UNSAT: {countUNSAT}")
print(f"Temps d'exécution        : {end - start:.3f} secondes")