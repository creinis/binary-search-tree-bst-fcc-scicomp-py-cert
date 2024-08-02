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




