class Node:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None

    def children(self):
        return [self.left_child, self.right_child]

class BST:
    def __init__(self):
        self.root = None

    def set_root(self, node):
        self.root = node

    def get_root(self, ):
        return self.root

    def get_root_val(self, ):
        return self.root.val

    def insert(self, val):
        if self.root is None:
            self.set_root(val)
        else:
            self.insert_node(self.root, val)

    def insert_node(self, current_node, node):
        if val <= current_node.val:
            if current_node.left_child:
                self.insert_node(current_node.left_child, val)
            else:
                current_node.left_child = Node(val)
        elif val > current_node.val:
            if current_node.right_child:
                self.insert_node(current_node.right_child, val)
            else:
                current_node.right_child = Node(val)
    
    def find(self, val):
        print("find(): " + str(val))
        return self.find_node(self.root, val)

    def find_node(self, current_node, val):
        # print("find_node(): " + str(val))
        print("in find_node() val: " + str(val) + " current_node.val: " + str(current_node.val))
        if current_node is None:
            return False
        elif val == current_node.val:
            return True
        elif val < current_node.val:
            return self.find_node(current_node.left_child, val)
        else:
            return self.find_node(current_node.right_child, val)