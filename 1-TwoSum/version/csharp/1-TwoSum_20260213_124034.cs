// Last updated: 13/02/2026, 12:40:34
1public class Solution {
2    public int[] TwoSum(int[] nums, int target) {
3
4        for (int i = 0; i < nums.Length; i++)
5        {
6            for (int j = i + 1; j < nums.Length; j++)
7            {
8                if (nums[i] + nums[j] == target)
9                    return new int[] { i, j };
10            }
11        }
12
13        return new int[0];
14    }
15}
16