// Last updated: 17/06/2025, 22:14:38
import java.util.*;

public class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(candidates); // Step 1: Sort the array
        backtrack(result, new ArrayList<>(), candidates, target, 0);
        return result;
    }

    private void backtrack(List<List<Integer>> result, List<Integer> tempList, int[] candidates, int remaining, int start) {
        if (remaining == 0) {
            result.add(new ArrayList<>(tempList));
        } else if (remaining > 0) {
            for (int i = start; i < candidates.length; i++) {
                // Step 2: Skip duplicates
                if (i > start && candidates[i] == candidates[i - 1]) continue;

                tempList.add(candidates[i]);
                backtrack(result, tempList, candidates, remaining - candidates[i], i + 1);
                tempList.remove(tempList.size() - 1); // Backtrack
            }
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

    }
}
