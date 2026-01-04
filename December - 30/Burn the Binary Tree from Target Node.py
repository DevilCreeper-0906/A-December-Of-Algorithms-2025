from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(10)
root.left = Node(21)
root.right = Node(24)

root.left.left = Node(14)
root.left.right = Node(15)

root.right.left = Node(12)
root.right.right = Node(22)

root.left.right.left = Node(23)
root.right.left.right = Node(13)

def map_parents(root):
    parent = {}
    q = deque([root])
    parent[root] = None
    while q:
        node = q.popleft()
        if node.left:
            parent[node.left] = node
            q.append(node.left)
        if node.right:
            parent[node.right] = node
            q.append(node.right)
    return parent


def find_target(root, target):
    if not root:
        return None
    if root.val == target:
        return root
    return find_target(root.left, target) or find_target(root.right, target)


def burn_tree(root, target):
    parent = map_parents(root)
    start = find_target(root, target)

    visited = set([start])
    q = deque([start])

    while q:
        size = len(q)
        level = []
        for _ in range(size):
            node = q.popleft()
            level.append(node.val)

            for nei in (node.left, node.right, parent[node]):
                if nei and nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        print(", ".join(map(str, level)))

target = int(input("Target: "))
burn_tree(root, target)
