// Last updated: 17/06/2025, 22:14:24
// Definition for a binary tree node.
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {}

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        // Create a list to hold the result of the traversal
        List<Integer> result = new ArrayList<>();
        // Helper method to perform the postorder traversal
        postorder(root, result);
        return result;
    }

    private void postorder(TreeNode node, List<Integer> result) {
        if (node == null) {
            return;
        }
        // Recur on the left subtree
        postorder(node.left, result);
        // Recur on the right subtree
        postorder(node.right, result);
        // Visit the root node
        result.add(node.val);
    }
}
