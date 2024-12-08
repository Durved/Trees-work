class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def build_tree(self, values):
        self.root = None
        for value in values:
            self.insert(value)

    def find_with_one_child(self):
        return self._find_with_one_child(self.root)

    def _find_with_one_child(self, node):
        result = []
        is_one_child = False

        if node.left is not None:
            result.extend(self._find_with_one_child(node.left))
            is_one_child = not is_one_child
        if node.right is not None:
            result.extend(self._find_with_one_child(node.right))
            is_one_child = not is_one_child

        if is_one_child:
            result.append(node.value)

        return result

    def find_leafs(self):
        return self._find_leaf(self.root)
    
    def is_balanced(self):
        return self._is_balanced(self.root)

    def _insert(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(value, node.right)

    def _find_leaf(self, node):
        result = []
        if node.left is None and node.right is None:
            return [node.value]
        if node.left is not None:
            result.extend(self._find_leaf(node.left))
        if node.right is not None:
            result.extend(self._find_leaf(node.right))
        return result
    
    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def _is_balanced(self, node):
        if node is None:
            return True
        
        left_height = self._height(node.left)
        right_height = self._height(node.right)

        if abs(left_height - right_height) > 1:
            return False

        return self._is_balanced(node.left) and self._is_balanced(node.right)
    
    
    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, node, level=0):
        if node is not None:
            self._print_tree(node.right, level + 1)
            print(' ' * level, node.value)
            self._print_tree(node.left, level + 1)
    
    

tree = Tree()
tree.build_tree(map(int, "7 3 2 1 9 5 4 6 8 0".split()[:-1]))
# tree.build_tree(map(int, "1 2 3 4 5 6 7 8 9 0".split()[:-1]))
# tree.print_tree()

# tree.build_tree(map(int, input().split()[:-1]))


print(*tree.find_with_one_child(), sep='\n')

# if tree.is_balanced():
#     print('YES')
# else:
#     print('NO')
