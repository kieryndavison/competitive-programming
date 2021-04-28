#include <map>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};

Node* copyRandomList(Node* head) {
    if (!head) {
        return NULL;
    }

    Node * newHead = new Node(head->val);
    map<Node *, Node *> randomPointers;
    randomPointers.insert(make_pair(head, newHead));
    
    Node *curOrignal = head->next;
    Node *curCopy = newHead;

    while (curOrignal) {
        Node * newNode = new Node(curOrignal->val);
        randomPointers.insert(make_pair(curOrignal, newNode));
        curCopy->next = newNode;
        curCopy = newNode;
        curOrignal = curOrignal->next;
    }
    
    curOrignal = head;
    curCopy = newHead;
        
    while (curCopy) {
        curCopy->random = curOrignal->random 
            ? randomPointers.find(curOrignal->random)->second : NULL;
        curCopy = curCopy->next;
        curOrignal = curOrignal->next;
    }
    
    return newHead;
}