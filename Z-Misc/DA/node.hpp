// Silly little node API

#pragma once

template<typename T>
struct Node{
    T val;
    Node<T>* next;
    Node<T>* prev;

    Node(T val) : val(val), next(nullptr), prev(nullptr) {}

    void set_next(Node<T>* nn) {
        this->next = nn;
    }

    void set_prev(Node<T>* pn) {
        this->prev = pn;
    }
};
