from collections import deque

Q = deque()

def max_levels(arr):
    levels = "asdf"


class Node:     # TreeNode
    def  __init__(self, key):
        if key == "null":
        self.data = None
        else:
        self.data = key
        self.left = None
        self.right = None


    def sum_levels(lst):
        levels = 0
        for i in range(10):
            if len(lst) == 2**i - 1:
                levels = i + 1 # number of levels is not 0-indexed
                break

        root = Node(lst[0])
        root.left = Node(lst[1])
        root.right = Node(lst[2])
        root.left.left = Node(lst[3])
        root.left.right = Node(lst[4])
        #root.right.left = Node(lst[5]) (we skip this to avoid problems)
        root.right.right = Node(lst[6])

"""
Breadth-first traversal

Q.add(root)
M.add(root)

while not isempty(Q):
	cur = Q.pop()
	V.append(cur)
	for child in cur.children:
		if child not in M:
	    	Q.add(child)	
			M.add(child)
"""
    Q = deque()
    V = []
    M = set()

  #add root to Q
    Q.appendleft(root)
  
    while len(Q) != 0:
        cur = Q.pop()
        V.append(cur)
        for child in [cur.left,cur.right]:
            if child not in M and child != None:
            Q.appendleft(child)	
                M.add(child)