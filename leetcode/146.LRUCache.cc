class LRUCache {
    int maxSize = 0;
    class Node {
    public:
        int key;
        int value;
        Node* next;
        Node* prev;
    };
    Node* head = NULL;
    Node* tail = NULL;
    map<int, Node*> position;

    void moveNodeToHead(Node* node) {
        if (node != head) {
            Node* curNode = node;
            if (node == tail) tail = node->prev;
            if (tail == head) tail->prev = curNode;
            node = node->next;
            curNode->next = head;
            curNode->prev = NULL;
            head = curNode;
        }
    }

public:
    LRUCache(int capacity) {
        maxSize = capacity;
    }
    
    int get(int key) {
        auto it = position.find(key);

        if (it != position.end()) {
            moveNodeToHead(it->second);
            return it->second->value;
        } else {
            return -1;
        }
    }
    
    void put(int key, int value) {
        auto it = position.find(key);

        if (it != position.end()) {
            moveNodeToHead(it->second);
            it->second->value = value;
        } else {
            Node* newNode = new Node();
            newNode->key = key;
            newNode->value = value;
            newNode->prev = NULL;
            newNode->next = head;

            if (position.size() == 0) {
                tail = newNode;
            } 
            
            if (position.size() == maxSize) {
                position.erase(tail->key);
                tail = tail->prev;
                if (tail != NULL) tail->next = NULL;
            }
            
            if (position.size() > 0) {
                head->prev = newNode;
            }
            
            head = newNode;
            position[key] = head;
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */