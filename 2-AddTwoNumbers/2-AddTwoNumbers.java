// Last updated: 17/06/2025, 22:14:55
public class Solution {

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode headNode = new ListNode();
        ListNode currentNode = headNode;
        int carryOver = 0;
        while (l1 != null || l2 != null || carryOver != 0){
            int val1 = 0, val2 = 0;
            if(l1 != null) val1 = l1.val;
            if(l2 != null) val2 = l2.val;
            int sum = val1 + val2 + carryOver;

            carryOver = sum/10;
            currentNode.next = new ListNode(sum % 10);

            currentNode = currentNode.next;
            if(l1 != null) l1 = l1.next;
            if(l2 != null) l2 = l2.next;
        }
        return headNode.next;
    }
}