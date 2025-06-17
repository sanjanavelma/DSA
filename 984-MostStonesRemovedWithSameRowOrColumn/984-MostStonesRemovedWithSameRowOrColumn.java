// Last updated: 17/06/2025, 22:13:59
import java.util.*;

class Solution {
    public int removeStones(int[][] stones) {
        int n = stones.length;
        boolean[] visited = new boolean[n];
        int numberOfConnectedComponents = 0;

        // Create an adjacency list for the graph
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }

        // Build the graph by connecting nodes (stones) that are in the same row or column
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (stones[i][0] == stones[j][0] || stones[i][1] == stones[j][1]) {
                    graph.get(i).add(j);
                    graph.get(j).add(i);
                }
            }
        }

        // Use DFS to find all connected components
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i, graph, visited);
                numberOfConnectedComponents++;
            }
        }

        // The maximum number of stones we can remove is n - numberOfConnectedComponents
        return n - numberOfConnectedComponents;
    }

    private void dfs(int node, List<List<Integer>> graph, boolean[] visited) {
        visited[node] = true;
        for (int neighbor : graph.get(node)) {
            if (!visited[neighbor]) {
                dfs(neighbor, graph, visited);
            }
        }
    }
}
