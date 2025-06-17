// Last updated: 17/06/2025, 22:14:04
class Solution {
    public int robotSim(int[] commands, int[][] obstacles) {
        // Direction vectors: North, East, South, West
        int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int x = 0, y = 0;  // Initial position
        int dir = 0;  // Start facing North
        int maxDistSq = 0;

        // Store obstacles in a set of strings for easy lookup
        Set<String> obstacleSet = new HashSet<>();
        for (int[] obstacle : obstacles) {
            obstacleSet.add(obstacle[0] + "," + obstacle[1]);
        }

        // Process each command
        for (int command : commands) {
            if (command == -2) {
                // Turn left (counterclockwise)
                dir = (dir + 3) % 4;
            } else if (command == -1) {
                // Turn right (clockwise)
                dir = (dir + 1) % 4;
            } else {
                // Move forward command units
                for (int i = 0; i < command; i++) {
                    int nextX = x + directions[dir][0];
                    int nextY = y + directions[dir][1];
                    
                    // Check for obstacle
                    if (!obstacleSet.contains(nextX + "," + nextY)) {
                        x = nextX;
                        y = nextY;
                        maxDistSq = Math.max(maxDistSq, x * x + y * y);
                    } else {
                        // Hit an obstacle, stop moving in this direction
                        break;
                    }
                }
            }
        }

        return maxDistSq;
    }
}