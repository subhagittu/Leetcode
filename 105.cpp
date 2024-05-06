class Solution {
    void createMap(vector<int> &in, unordered_map<int,int> &map, int &n){
        for(int i=0; i<n; i++){ 
            map[in[i]] = i; 
        }  
    }
 

    TreeNode* build(vector<int> &pre, vector<int> &in, int &index, int inStart, int inEnd, int &n, unordered_map<int,int> &map){
        if(index>=n || inStart>inEnd) return NULL;

        int element = pre[index++];
        TreeNode* root = new TreeNode(element);
        int pos = map[element];

        root->left = build(pre,in,index,inStart,pos-1,n,map);
        root->right = build(pre,in,index,pos+1,inEnd,n,map);
        return root;
    }
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int preIndex = 0;
        int n = preorder.size();
        unordered_map<int,int> mapping;
        createMap(inorder,mapping,n);
        return build(preorder,inorder,preIndex,0,n-1,n,mapping);
    }
};
