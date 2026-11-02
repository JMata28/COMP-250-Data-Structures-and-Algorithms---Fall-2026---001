#Code from https://www.w3schools.com/dsa/dsa_data_binarytrees.php
#Useful videos to undertand tree data structures:
#https://www.youtube.com/watch?v=1-l_UOFi1Xw&t=13s
#https://www.youtube.com/watch?v=EPwWrs8OtfI 

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG


#Let's now see how to traverse this code using BFS. 
from collections import deque

def bfs_traverse(root):
    if root is None:
        return

    result = []
    queue = deque([root])
    
    while queue:
        level = [] #create new list for this level
        q_length = len(queue)

        for _ in range(q_length):
            node = queue.popleft() 
            level.append(node.data)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        result.append(level) #add level list to our final result list

    return result

print(bfs_traverse(root))