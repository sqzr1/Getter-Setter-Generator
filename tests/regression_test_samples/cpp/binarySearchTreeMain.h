// BinaryTree.h - class definition of the binary tree data type 
// Written by Michael Mikulski 
 
#pragma once 
 
template<typename T> struct TreeNode 
{ 
    // Initi constructor 
    TreeNode(const T& value, TreeNode<T>* left = NULL, TreeNode<T>* right = NULL) 
    { 
        Value = value; 
        Left = left; 
        Right = right; 
    } 
 
    ~TreeNode() 
    { 
        //delete Left; 
        //delete Right; 
    } 
 
    T Value; 
    TreeNode<T>* Left; 
    TreeNode<T>* Right; 
 
    // if the current TreeNode is a leaf 
    bool IsLeaf() const 
    { 
        return (Left == NULL) && (Right == NULL); 
    } 
};
