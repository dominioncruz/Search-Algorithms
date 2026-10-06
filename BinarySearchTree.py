class BST:
    def __init__(self,data):
        # Initialize a node in the Binary Search Tree (BST) with a value and set left and right child nodes to None
        self.value = data
        self.left = None
        self.right = None

def create_BST(node, value):
    # Function to create a Binary Search Tree (BST) recursively

    # Check if the value already exists in the current node, if yes, return as there's no need to insert duplicate values
    if node.value == value:
        return

    # If the value is less than the current node's value, traverse to the left subtree
    if (value < node.value):
        # Check if the left child of the current node is not None
        if(node.left != None):
            # If not None, recursively call create_BST function with the left child node and the value to be inserted
            create_BST(node.left, value)
        else:
            # If the left child is None, create a new node with the given value and assign it as the left child of the current node
            the_new_node = BST(value)
            node.left = the_new_node

    # If the value is greater than the current node's value, traverse to the right subtree
    else:
        # Check if the right child of the current node is not None
        if (node.right != None):
            # If not None, recursively call create_BST function with the right child node and the value to be inserted
            create_BST(node.right, value)
        else:
            # If the right child is None, create a new node with the given value and assign it as the right child of the current node
            the_new_node = BST(value)
            node.right = the_new_node

# Sample data for creating the Binary Search Tree
s = [4,2,7,8,6,75]

# Create the root node of the Binary Search Tree
node_one = BST(4)

# Iterate through the sample data, excluding the first element (already assigned as root)
for each_value in s[1:]:
    # Call create_BST function to insert each value into the Binary Search Tree
    create_BST(node_one, each_value)
