/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    
    ListNode* removeNthFromEnd(ListNode* a, int k) {

        ListNode *dummy=new ListNode(0,a),*b=dummy, *del;

        // kth node from end is (n-k)th node from start.
        int K,n=0;
        while(b)b=b->next,n++;
        
        // K = n-k-1. node next to this (del) Kth needs to be deleted
        K=n-k-1, b=dummy;
        while(K--!=0) b=b->next;

        del=b->next;
        b->next=del->next;
        delete(del);

        return dummy->next;
    }
};