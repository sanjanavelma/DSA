// Last updated: 17/06/2025, 22:14:40
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> tempList = new ArrayList<>();
        Arrays.sort(candidates); // Sort to handle duplicates
        backtrack(result, tempList, candidates, target, 0);
        return result;
    }

    private void backtrack(List<List<Integer>> result, List<Integer> tempList, int[] candidates, int remaining, int start) {
        if (remaining < 0) return; // If the remaining sum is less than zero, no valid combination can be formed
        if (remaining == 0) {
            result.add(new ArrayList<>(tempList));
            return;
        }

        for (int i = start; i < candidates.length; i++) {
 
            if (i > start && candidates[i] == candidates[i - 1]) continue;
            tempList.add(candidates[i]);

            backtrack(result, tempList, candidates, remaining - candidates[i], i);
            tempList.remove(tempList.size() - 1); // Backtrack to explore other possibilities
        }
    }
}

