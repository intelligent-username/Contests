// Linked Lists

#include "node.hpp"

template<typename T>
class LinkedList {
    private:
        Node<T>* first;
        Node<T>* last;
    
    public:
        LinkedList(): first(nullptr), last(nullptr){}
        LinkedList(Node<T>* a): first(a), last(a){}
        LinkedList(Node<T>* a, Node<T>* b): first(a), last(b) {}

        void append_node(Node<T>* n) {
            last->next = n;
            last = n;
        }
        Node<T>* pop() {
            Node<T>* temp = first;
            first = first->next;
            return temp;
        }

};
