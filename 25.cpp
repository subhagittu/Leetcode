class Solution {
public:
    int length(ListNode* head){
        int count=0;
        while(head){
            count++;
            head= head->next;
        }
        return count;
    }

    ListNode*solve(ListNode*head, int k, int size){
        int count = 0;
        ListNode* curr = head, * prev = NULL,* nxt = NULL;
        while(count < k && curr){
            nxt = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nxt;
            count++;
        }
        size -= k;

        if(nxt && size >= k){
            head->next = solve(nxt , k, size);
        }
        else head->next = nxt;
        return prev;
    }
    
    ListNode* reverseKGroup(ListNode* head, int k) {
        return solve(head, k, length(head));
    }
};
