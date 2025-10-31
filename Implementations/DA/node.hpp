// Silly little node API

#pragma once

template<typename T>

struct Node{
    T val;
    Node<T>* next;
    Node<T>* prev;

    Node(T val);
    void set_next(Node<T>* nn);
    void set_prev(Node<T>* pn);

};

#include "node.tpp"
