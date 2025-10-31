#include "node.hpp"
// This is a circular import only for the sake of geting rid of the red squigglesevery time I mention Node<T> 
// It won't break anything due to the pragma once
// Lesson learnt: try not to use generic types

template<typename T>
Node<T>::Node(T val) : val(val), next(nullptr), prev(nullptr) {}

template<typename T>
void Node<T>::set_next(Node<T>* nn) {
    this->next = nn;
}

template<typename T>
void Node<T>::set_prev(Node<T>* pn) {
    this->prev = pn;
}
