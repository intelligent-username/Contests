// (Doubly) Linked Lists

#include "node.hpp"
#include <optional>
#include <stdexcept>

using namespace std;

template<typename T>
class LinkedList {
    private:
        Node<T>* first;
        Node<T>* last;
        int size;
    
    public:

        LinkedList(): first(nullptr), last(nullptr), size(0){}

        LinkedList(Node<T>* a): first(a), last(a), size(1){
            if (a) {
                first->prev = nullptr;
                last->next = nullptr;
            } else {
                first = nullptr;
                last = nullptr;
                size = 0;
            }
        }

        LinkedList(Node<T>* a, Node<T>* b): first(a), last(b){
            if (a && b) {
                a->next = b;
                b->prev = a;
                first->prev = nullptr;
                last->next = nullptr;
                
                first = a;
                last = b;
                
                size = 2;

            } else if (a) {
                a->next = nullptr;
                a->prev = nullptr;
                first = a;
                last = a;
                size = 1;

            } else if (b) {
                b->next = nullptr;
                b->prev = nullptr;
                first = b;
                last = b;
                size = 1;

            } else {
                first = nullptr;
                last = nullptr;
                size = 0;
            }
        }

        ~LinkedList() {
            Node<T>* current = first;
            while (current != nullptr) {
                Node<T>* next_node = current->next;
                delete current;
                current = next_node;
            }
            first = nullptr;
            last = nullptr;
            size = 0;
        }

        void append(Node<T>* n) {
            if (n == nullptr) {
                return;
            }
            n->next = nullptr;
            n->prev = nullptr;

            if (!first) {
                first = n;
                last = n;
            } else {
                last->next = n;
                n->prev = last;
                last = n;
            }
            size++;
        }

        void prepend(Node<T> *n) {
            if (n == nullptr) {
                return;
            }

            n->next = nullptr;
            n->prev = nullptr;

            if (!first) {
                first = n;
                last = n;
            } else {
                n->next = first;
                first->prev = n;
                first = n;
            }
            size++;
        }

        optional<T> pop() {
            if (size == 0) {
                return nullopt;
            }

            Node<T>* node_to_remove = first;
            T val_to_return = node_to_remove->val;

            if (size == 1) {
                first = nullptr;
                last = nullptr;
            } else {
                first = first->next;
                first->prev = nullptr;
            }
            
            delete node_to_remove;
            size--;
            return val_to_return;
        }

        optional<T> pop_back() {
            if (size == 0) {
                return nullopt;
            }

            Node<T>* node_to_remove = last;
            T val_to_return = node_to_remove->val;

            if (size == 1) {
                first = nullptr;
                last = nullptr;
            } else {
                last = last->prev;
                last->next = nullptr;
            }

            delete node_to_remove;
            size--;
            return val_to_return;
        }

        optional<T> peek_top(){
            if (!first) {
                return nullopt;
            }
            return first->val;
        }

        optional<T> peek_back() {
            if (!last) {
                return nullopt;
            }
            return last->val;
        }

        bool is_empty() const {
            return size == 0;
        }

        int get_size() const {
            return size;
        }
};
