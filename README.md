# Certifying-algorithm-thesis

Les fichiers expérimentaux implémentant les différentes partie d'un Algorithme Certifiant sont les fichiers commencant par "Exemple" :

- Hamilton, Clique et kColor pour tester la conversion de rgaphe en format SAT.

- ExempleSAT pour vérifier si un modèle donné est solution d'un problème.

- ExempleUNSAT pour créer une preuve DRAT lorsqu'un problème ne possède pas de solutions.

Les fichiers présent dans le dossier CertifyingAlgo sont le coeur du code :

- NkColor, Nclique et hamilton permettent de convertir un graphe en ensemble de clauses SAT selon le problème souhaité.

- CDCL contient l'algorithme du même nom pour trouver une assignation possible de variable s'il en existe une.

- SATChecker se charge de vérifier si une assignation de valeurs est solution d'un problème donné. Il s'occupe également de fournir une preuve DRAT si aucune solution n'est possible.

Les deux fichiers .txt sont des exemple de preuve DRAT fournie par les algorithmes.