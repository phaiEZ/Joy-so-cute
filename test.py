class TreeNode(object):

    def __init__(self, x):

        self.val = x

        self.left = None

        self.right = None



def list_to_bst(list_num):
    if not list_num:
        return None
    mid = int(len(list_num) / 2)
    node = TreeNode(list_num[mid])
    node.left = list_to_bst(list_num[:mid])
    node.right = list_to_bst(list_num[mid+1:])
    return node



def preOrder(node): 

    if not node: 

        return      

    print(node.val)

    preOrder(node.left) 

    preOrder(node.right)   



def printBST(node,level = 0):

    if node != None:

        printBST(node.right, level + 1)

        print('     ' * level, node.val)

        printBST(node.left, level + 1)



list_nums = sorted([int(item) for item in input("Enter list : ").split()])

result = list_to_bst(list_nums)



print("\nList to a height balanced BST : ")

print(preOrder(result))

print("\nBST model : ")

printBST(result)