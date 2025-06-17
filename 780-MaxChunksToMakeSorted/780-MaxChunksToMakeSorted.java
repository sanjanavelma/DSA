// Last updated: 17/06/2025, 22:14:07
class Solution {
    public int maxChunksToSorted(int[] arr) {
        int max = 0; int ans = 0; int n = arr.length;
        for(int i=0; i<n; i++){
            if(max<arr[i]){
                max=arr[i];
            }
            if(max==i){
                ans++;
            }
        }
        return ans;
    }
}