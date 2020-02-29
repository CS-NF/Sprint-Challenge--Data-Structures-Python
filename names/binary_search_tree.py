class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree

    # *** Plan ***
    # if the value is greater then the given index
    # self.left is going to equal the index in the Binary Search Tree
    # else we call the function recursivly
    # if the value is less then the given index
    # append self.value to the left 
    def insert(self, i):
        if i < self.value: # if the value is greater then the given index we will exicture the code below
            if not self.left: # if it's not the left part of the binary tree
                self.left = BinarySearchTree(i) # we assign to the left part of the binary search tree
            else:
               self.left.insert(i) # otherwise we will add (i == our value) to the left of the binary search tree 
        else:
            if not self.right:
                self.right = BinarySearchTree(i) # we assign to the right part of the binary search tree
            else:
                self.right.insert(i) # otherwise we will add (i == our value) to the right of the binary search tree
        


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target: # if our value is equal to our arugment
            return True
        if target < self.value: # check to see if the target is less then our value
          if self.left: # check left 
              return self.left.contains(target) # our node get's recursively called on the left side of the tree beacuse it's smaller then (head/root)
          else:
              return False # It's fales beacuse it's bigger then our value (head/root)
        if target >= self.value: # if the target is grater then 
            if self.right: # check to see if the target is greater then our value
                return self.right.contains(target) # our node get's recursively called on the right side of the tree beacuse it's greater then (head/root) 
            else:
                return False # It's fales beacuse node is smaller then our value (head/root)