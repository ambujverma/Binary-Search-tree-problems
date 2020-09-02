import queue
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 
        self.hd = 0

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
def height(root):
    if root:
        return(1+max(height(root.left),height(root.right)))
    else:
        return -1

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.info,end=' ')
        inOrder(root.right)

def preOrder(root):
    if root:
        print(root.info,end=' ')
        preOrder(root.left)
        preOrder(root.right)
        
        
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.info,end=' ')

def levelorder(root):
    
    if root is None:
        return 0
    q=[]
    q.append(root)
    while len(q)>0:
        
        print(q[0].info,end =' ')
        node = q.pop(0)
        
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)        

def topview(root):
    if root == None:
        return
    q=[]
    m=dict()
    hd=0
   
    
    q.append(root)
    while(len(q)):
        root = q[0]
        hd = root.hd
        
        if hd not in m:
            m[hd] = root.info
        if root.left:
            root.left.hd = hd-1
            q.append(root.left)
            
        if root.right:
            root.right.hd = hd+1
            q.append(root.right)
            
        q.pop(0)
    for i in sorted (m):
        print(m[i],end=' ')
        
        
def lca(root,n1,n2):
    if root is None:
        return
    if root.info > n1 and root.info > n2:
        return lca(root.left,n1,n2)
    if root.info < n1 and root.info < n2:
        return lca(root.right,n1,n2)
    return(root)
        
   
                    

tree = BinarySearchTree()
t = int(input())
arr = list(map(int, input().split()))
for i in range(t):
    tree.create(arr[i])
    
    
print('height of tree==',height(tree.root))

print('inorder traversal',inOrder(tree.root))

print('preorder traversal',preOrder(tree.root))

print('postorder traversal',postOrder(tree.root))

print('level order traversal',levelorder(tree.root))

print("top view of binary search tree",topview(tree.root))

print('lowest common ancestor==',lca(tree.root,4,14))
