# Heaps

This is for solving Heap Problems

## What to remember

- Heaps are complete binary trees
- Heap property: all children are less than or equal to (or geq) their parents, depending on if it's a max heap or min heap
- Heapify: maintaining the heap property

  - When inserting, insert in the "next" position for maintaining the balanced binary tree property
  - Then sift up to maintain the heap property

  - When popping, delete the root, swap it with the last element so as to maintain the balanced binary tree property
  - Then sift down to maintain the heap property
