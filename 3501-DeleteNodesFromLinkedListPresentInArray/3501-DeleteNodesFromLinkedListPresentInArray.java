// Last updated: 17/06/2025, 22:13:06
import java.util.HashSet;

class Solution {
    public ListNode modifiedList(int[] nums, ListNode head) {
        // Convert nums array to a set for O(1) lookups
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        
        // Create a dummy node to handle cases where head needs to be removed
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode current = dummy;
        
        // Traverse the list and remove nodes whose values are in the set
        while (current.next != null) {
            if (set.contains(current.next.val)) {
                current.next = current.next.next;  // Skip over the node
            } else {
                current = current.next;  // Move to the next node
            }
        }
        
        return dummy.next;  // Return the modified list, starting from head
    }
}
