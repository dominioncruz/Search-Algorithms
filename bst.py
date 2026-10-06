class BST:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None
        
    def height(self, node):
    
        if self == None:
            return 0
        
        return 1 + max(self.height(self.left), self.height(self.right))

def create_BST(node, value):

    if node.value == value:
        return
            
    if(value < node.value):
        if(node.left != None):
            create_BST(node.left, value)
        else:
            the_new_node = BST(value)
            node.left = the_new_node

    else:
        if(node.right != None):
            create_BST(node.right, value)
        else:
            the_new_node = BST(value)
            node.right = the_new_node

s = [4, 2, 7, 8, 6, 75]

node_one = BST(4) #Creating the head node

for each_value in s[1:]:
    create_BST(node_one, each_value)


def via_inorder(node):
    if node == None:
        return[]
    
    print(via_inorder(node.left) + [node.value] + via_inorder(node.right))
    
    
def pre_order(node):
    if node == None:
        return[]
    
    print([node.value] + pre_order(node.left) + pre_order(node.right))
    
def post_inorder(node):
    if node == None:
        return[]
    
    print(post_inorder(node.left) + post_inorder(node.right) + [node.value])
    



print(node_one.height(node_one.value))
    
    
    

