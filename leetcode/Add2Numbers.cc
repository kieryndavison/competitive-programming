//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* sum = NULL;
        ListNode* cur = NULL;
        ListNode* temp1 = l1;
        ListNode* temp2 = l2;
        int carry = 0;
        
        while ( temp1 != NULL && temp2 != NULL ) {
            int val = temp1->val + temp2->val + carry;
            int digit = val % 10;
            carry = val / 10;
            if ( sum == NULL ) {
                sum = new ListNode( digit );
                cur = sum;
            } else {
                cur->next = new ListNode( digit );
                cur = cur->next;
            }
            temp1 = temp1->next;
            temp2 = temp2->next;
        }
        
        while (temp1 != NULL) {
            int val = temp1->val + carry;
            int digit = val % 10;
            carry = val / 10;
            if ( sum == NULL ) {
                sum = new ListNode( digit );
                cur = sum;
            } else {
                cur->next = new ListNode( digit );
                cur = cur->next;
            }
            temp1 = temp1->next;
        }
        
        while (temp2 != NULL) {
            int val = temp2->val + carry;
            int digit = val % 10;
            carry = val / 10;
            if ( sum == NULL ) {
                sum = new ListNode( digit );
                cur = sum;
            } else {
                cur->next = new ListNode( digit );
                cur = cur->next;
            }
            temp2 = temp2->next;
        }
        
        if ( carry ) {
            cur->next = new ListNode( carry );
        }
        
        return sum;
    }
};