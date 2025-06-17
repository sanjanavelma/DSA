// Last updated: 17/06/2025, 22:13:54
import java.util.*;

class Solution {
    public double maxProbability(int n, int[][] edges, double[] succProb, int start, int end) {
        // Graph representation: adjacency list
        List<Map<Integer, Double>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new HashMap<>());
        }
        
        // Populate the graph
        for (int i = 0; i < edges.length; i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            double prob = succProb[i];
            graph.get(u).put(v, prob);
            graph.get(v).put(u, prob);
        }
        
        // Max-Heap to always explore the highest probability first
        PriorityQueue<double[]> pq = new PriorityQueue<>((a, b) -> Double.compare(b[1], a[1]));
        pq.offer(new double[]{start, 1.0});
        
        // To store the maximum probability to reach each node
        double[] maxProb = new double[n];
        maxProb[start] = 1.0;
        
        while (!pq.isEmpty()) {
            double[] current = pq.poll();
            int node = (int) current[0];
            double prob = current[1];
            
            // If we reached the end node, return the probability
            if (node == end) {
                return prob;
            }
            
            // Explore neighbors
            for (Map.Entry<Integer, Double> entry : graph.get(node).entrySet()) {
                int neighbor = entry.getKey();
                double edgeProb = entry.getValue();
                
                // Calculate the probability via the current node
                double newProb = prob * edgeProb;
                if (newProb > maxProb[neighbor]) {
                    maxProb[neighbor] = newProb;
                    pq.offer(new double[]{neighbor, newProb});
                }
            }
        }
        
        // If we never reach the end node
        return 0.0;
    }
}
