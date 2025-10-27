name = "Sohan R"
usn = "1BM23CS336"

import math

class Node:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.children = []
        self.pruned = False

def alpha_beta(node, depth, alpha, beta, maximizing_player):
    if not node.children:  # leaf node
        return node.value

    if maximizing_player:
        max_eval = -math.inf
        for child in node.children:
            eval = alpha_beta(child, depth + 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                child.pruned = True
                break
        node.value = max_eval
        return max_eval
    else:
        min_eval = math.inf
        for child in node.children:
            eval = alpha_beta(child, depth + 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                child.pruned = True
                break
        node.value = min_eval
        return min_eval

def print_tree(node, level=0):
    prefix = "   " * level + "└── "
    if node.pruned:
        print(f"{prefix}{node.name} (PRUNED)")
    else:
        if node.children:
            val = node.value if node.value is not None else "-"
            print(f"{prefix}{node.name} [Value={val}]")
            for child in node.children:
                print_tree(child, level + 1)
        else:
            print(f"{prefix}{node.name} [Leaf={node.value}]")

leaf_values = [3, 5, 6, 9, 1, 2, 0, -1]

root = Node("A")
b = Node("B")
c = Node("C")
root.children = [b, c]

b1 = Node("B1")
b2 = Node("B2")
c1 = Node("C1")
c2 = Node("C2")
b.children = [b1, b2]
c.children = [c1, c2]

b1.children = [Node("L1", leaf_values[0]), Node("L2", leaf_values[1])]
b2.children = [Node("L3", leaf_values[2]), Node("L4", leaf_values[3])]
c1.children = [Node("L5", leaf_values[4]), Node("L6", leaf_values[5])]
c2.children = [Node("L7", leaf_values[6]), Node("L8", leaf_values[7])]

print("==============================")
print("      ALPHA-BETA PRUNING")
print("==============================")
print(f"\nLeaf Node Values: {leaf_values}\n")

result = alpha_beta(root, 0, -math.inf, math.inf, True)

print("==============================")
print(f"Value of Root Node (MAX): {result}")
print("==============================")

print("\nTREE STRUCTURE (with pruning):")
print_tree(root)

print("\n------------------------------")
print(f"Name : {name}")
print(f"USN  : {usn}")
print("------------------------------")
