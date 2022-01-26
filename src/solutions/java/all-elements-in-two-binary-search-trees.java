/*
#1305
https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
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
    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        Stack<TreeNode> nodesList1 = new Stack<TreeNode>();
        Stack<TreeNode> nodesList2 = new Stack<TreeNode>();
        List<Integer> res = new ArrayList<Integer>();
        
        getNextElements(root1, nodesList1);
        getNextElements(root2, nodesList2);

        while(!nodesList1.empty() || !nodesList2.empty())
        {
            int firstVal = 100001, secondVal = 100001;
            if(!nodesList1.empty()) firstVal = nodesList1.peek().val;
            if(!nodesList2.isEmpty()) secondVal = nodesList2.peek().val;
            
            if(firstVal <= secondVal){
                TreeNode node = nodesList1.pop();
                res.add(firstVal);
                getNextElements(node.right, nodesList1);
            }
            else{
                TreeNode node = nodesList2.pop();
                res.add(secondVal);
                getNextElements(node.right, nodesList2);
            }
        }
        return res;
    }
    private void getNextElements(TreeNode node, Stack s)
    {
        while(node != null){
            s.push(node);
            node = node.left;
        }
    }
}