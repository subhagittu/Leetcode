class Solution {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        if (root == null)
            return new ArrayList<>();
        
        List<List<Integer>> res = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();
        q.push(root);
        
        while (!q.isEmpty()) {
            int count = q.size();
            List<Integer> v = new ArrayList<>();
            
            for (int i = 0; i < count; i++) {
                TreeNode curr = q.poll();
                
                if (curr.left != null)
                    q.push(curr.left);
                if (curr.right != null)
                    q.push(curr.right);
                v.add(curr.val);
            }
            res.add(v);
        }
        Collections.reverse(res);
        return res;
    }
}