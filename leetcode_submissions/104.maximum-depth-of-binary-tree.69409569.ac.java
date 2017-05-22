/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *   int val;
 *   TreeNode left;
 *   TreeNode right;
 *   TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
  public int depth = 0;
  public int maxDepth(TreeNode root) {
    if (root == null) return 0;
    else depth = 1;
    DFS(root, 1);
    return depth;
  }
  
  public void DFS(TreeNode root, int level) {
    if(root == null) return;
    if(level > depth) depth = level;
    if(root.left != null){
      DFS(root.left, level+1);
    }
    if(root.right != null) {
      DFS(root.right, level+1);
    }
  }
  
}