# Certifying-algorithm-thesis

librairies importantes : glocose3, networkX, pysat

Les fichiers expérimentaux implémentant les différentes partie d'un Algorithme Certifiant sont les fichiers commencant par "Exemple" :

- Hamilton, Clique et kColor pour tester la conversion de rgaphe en format SAT.

- ExempleSAT pour vérifier si un modèle donné est solution d'un problème.

- ExempleUNSAT pour créer une preuve DRAT lorsqu'un problème ne possède pas de solutions.

Note : Les testeurs SAT et UNSAT ne fonctionnent pas sur windown et mac.

Les fichiers présent dans le dossier CertifyingAlgo sont le coeur du code :

- NkColor, Nclique et hamilton permettent de convertir un graphe en ensemble de clauses SAT selon le problème souhaité.

- CDCL contient l'algorithme du même nom pour trouver une assignation possible de variable s'il en existe une.

- SATChecker se charge de vérifier si une assignation de valeurs est solution d'un problème donné. Il s'occupe également de fournir une preuve DRAT si aucune solution n'est possible.

ExempleNetworkX utilise un code en format graph6 pour générer un graphe et utilise l'algorithme KColor dessus

Les deux fichiers .txt sont des exemple de preuve DRAT fournie par les algorithmes.