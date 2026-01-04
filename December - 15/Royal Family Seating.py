from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree(values):
    if not values or values[0] == -1:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        if values[i] != -1:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] != -1:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root


def isCompleteTree(root):
    if not root:
        return True

    queue = deque([root])
    seen_none = False

    while queue:
        node = queue.popleft()

        if node is None:
            seen_none = True
        else:
            if seen_none:
                return False
            queue.append(node.left)
            queue.append(node.right)

    return True


N = int(input("Enter number of nodes: "))
values = list(map(int, input("Enter node values (-1 for NULL): ").split()))

root = build_tree(values)

result = isCompleteTree(root)
print(result)
