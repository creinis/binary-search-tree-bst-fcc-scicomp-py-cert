# Binary Search Tree - BST

# Step 1

# In this project, you are going to create a Binary Search Tree (BST). 
# A BST is a data structure in which each node has at most two children, with the left child containing values 
# less than the parent node and the right child containing values greater than the parent node, allowing for 
# efficient searching and sorting operations.

# This is what a Binary Search Tree looks like:

# Begin by defining an empty TreeNode class. The TreeNode class represents a node in a binary search tree. 
# Use the pass keyword to fill the class body and avoid an error.

class TreeNode():
    pass

# Step 2

# Inside the TreeNode class, replace pass with an __init__ method so that you can initialize the attributes 
# of the object. Don't add any parameters and use the pass keyword to avoid an error.

class TreeNode:
    def __init__():
        pass

# Step 3

# The __init__ method takes two parameters: self (which represents the instance of the class being created) 
# and key (the value to be stored in the node). Add those two parameters to the __init__() method.

class TreeNode:
    def __init__(self, key):
        pass

# Step 4

# Inside the __init__ method, delete pass and assign the value of the key parameter to the key attribute of the 
# node using self.key.

# This means that the key attribute of the TreeNode instance will be set to the value passed during the 
# object's creation.

class TreeNode:
    def __init__(self, key):
        self.key = key

# Step 5

# Inside the __init__ method, initialize the left and right attributes of the node to None. 
# This is because when a node is first created, it doesn't have any left or right children. 
# Remember to use the self keyword.

class TreeNode:    
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Step 6

# Create another empty class called BinarySearchTree that represents a binary search tree.

class BinarySearchTree :
    pass

# Step 7

# Within the BinarySearchTree class, replace pass with an __init__ method and add a self parameter to this method.

class BinarySearchTree:
    def __init__(self):
        pass

# Step 8

# Inside the __init__ method, delete pass and initialize an instance attribute called root to the value None.

# The root attribute represents the root node of the binary search tree. 
# Since this is the constructor when a new BinarySearchTree object is created, it starts with an empty tree, 
# so the root attribute is set to None.

class BinarySearchTree:
    def __init__(self):
        self.root = None

# Step 9

# Next, you need to define a mechanism to insert nodes in the tree. 
# For that, define an empty insert method within the BinarySearchTree class and give it a self parameter.

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self):
        pass

# Step 10

# The insert method will be called by the user. 
# In addition to the self parameter, it will also need a key parameter. 
# This parameter will be the key value to insert into the binary search tree.

# Add key as the second parameter to the function definition.

# Step 11

# Now, inside the insert method, you need to call another method _insert() that performs the actual insertion. 
# You are going to define the _insert method soon.

# Delete pass and assign self._insert(self.root, key) to self.root.

# Note that:

#    self.root passes the root node of the tree as the first argument. This is the starting point for the insertion process.
#    key: passes the key value you want to insert as the second argument.

    def insert(self,key):
        self.root = self._insert(self.root, key)

# Step 12

# Now you are going to define an _insert method, which is a helper function and does the actual insertion. 
# This method is recursive, meaning it calls itself to traverse the tree until the appropriate location for 
# the new node is found.

# Define an _insert method with the parameters self, node and key.

    def _insert(self, node, key):
        pass

# Step 13

# Now you need to check if the node parameter is None. If it is, this means that the method has reached a 
# leaf node or an empty spot in the tree where the new node should be inserted.

# Inside the method body, write an if statement that checks if node is None. 
# Inside the if block, return TreeNode(key) to create a new TreeNode instance with the provided key. 
# This will become the new leaf node, effectively inserting the key into the tree.

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)

# Step 14

# Now you need to recursively traverse the tree and insert the values using the principle for binary trees:

#    Values smaller than the key are placed in the left subtree
#    Values greater than the key are placed in the right subtree

# After your existing conditional statement, write another if statement to check if key is strictly less than node.key.

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            pass  




