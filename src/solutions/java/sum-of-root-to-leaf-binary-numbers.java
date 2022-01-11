/*
#1022
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
*/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private int res = 0;
    public int sumRootToLeaf(TreeNode root) {
        if(root != null)
            dfs(root, 0);
        return res;
    }
    private void dfs(TreeNode root, int soFar)
    {
        int curr =  (soFar * 2) + root.val;
        if(root.left == null && root.right == null)
        {
            res += curr;
            return;
        }
        if(root.left != null)
            dfs(root.left, curr);
        if(root.right != null)
            dfs(root.right, curr);
    }
}