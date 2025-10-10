import java.util.*;

public class ChordalGraphCertifier {

    // Method to check if a graph is chordal
    public static boolean isChordal(int[][] graph) {
        int n = graph.length;
        List<Integer> eliminationOrder = new ArrayList<>();
        boolean[] visited = new boolean[n];

        // Perform a greedy elimination ordering
        for (int i = 0; i < n; i++) {
            int vertex = findNextVertex(graph, visited);
            if (vertex == -1) return false; // No valid vertex found
            eliminationOrder.add(vertex);
            visited[vertex] = true;
        }

        // Verify the elimination order
        if (verifyEliminationOrder(graph, eliminationOrder)) {
            System.out.println("Graph is chordal. Elimination order: " + eliminationOrder);
            return true;
        } else {
            System.out.println("Graph is not chordal.");
            return false;
        }
    }

    // Find the next vertex for elimination
    private static int findNextVertex(int[][] graph, boolean[] visited) {
        for (int i = 0; i < graph.length; i++) {
            if (!visited[i]) return i; // Simplified for demonstration
        }
        return -1;
    }

    // Verify the elimination order
    private static boolean verifyEliminationOrder(int[][] graph, List<Integer> order) {
        Set<Integer> laterNeighbors = new HashSet<>();
        for (int vertex : order) {
            laterNeighbors.clear();
            for (int i = 0; i < graph.length; i++) {
                if (graph[vertex][i] == 1 && order.indexOf(i) > order.indexOf(vertex)) {
                    laterNeighbors.add(i);
                }
            }
            if (!isClique(graph, laterNeighbors)) return false;
        }
        return true;
    }

    // Check if a set of vertices forms a clique
    private static boolean isClique(int[][] graph, Set<Integer> vertices) {
        for (int v1 : vertices) {
            for (int v2 : vertices) {
                if (v1 != v2 && graph[v1][v2] == 0) return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        // Example adjacency matrix for a chordal graph
        int[][] graph = {
            {0, 1, 1, 0},
            {1, 0, 1, 1},
            {1, 1, 0, 1},
            {0, 1, 1, 0}
        };

        isChordal(graph);
    }
}
