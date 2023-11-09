class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
      
        if(!head) return NULL;
        if(!head->next) return new TreeNode(head->val);

       
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* Prev = NULL;

        while(fast && fast->next){
            Prev = slow;
            fast = fast->next->next;
            slow = slow->next;
        }

       
        ListNode* Middle = slow;
        Prev->next = NULL;

        TreeNode* root = new TreeNode(Middle->val);
        root->left = sortedListToBST(head);
        root->right = sortedListToBST(Middle->next);

        
        return root;
    }
};
