# coding: utf-8
"""
Script to creat and manipulate binary tree of nodes
"""


class TreeNode:
    """
    Class of methods to creat and print the binary tree.
    """
    def __init__(self: object, data):
        """
        Methode establishing the binary tree, by
        creating a list of nodes objects of integer.

        @data : node value
        """
        self.data = data
        self.right_child = None
        self.left_child = None
        self.level = 0

    def print_treenode(self):
        """
        Methode to print the binary tree's representation of the node objects
        """
        if self.right_child:
            self.right_child.print_treenode()
        print(self.data)
        if self.left_child:
            self.left_child.print_treenode()

    def is_leaf(self):
        """
        :return:
        """
        return self.right_child is None and self.left_child is None

    def __str__(self):
        """
        Return a string representation of the tree's leafs
        """
        if self.is_leaf():
            return str(self.data)
        else:
            return "[" + str(self.left_child) + ";" + str(self.right_child) + "]:" + str(self.data)


class Tree:
    """
    Class of methods to creat and perform actions of insertion and/or deletion
    of nodes in the binary tree.
    """
    def __init__(self: object, root_node):
        """
        Constructor to initiate the node value of the tree's root.
        :param root_node: root's value
        """
        self.root_node = root_node

    def traversal_deep(self):
        """
        :return:
        """
        print(self.root_node)

    def node_can_be_added(self, target_node):
        """
        Methode to check if the child's node is empty
        :param target_node: searched node
        :return: the empty child right or left
        """
        return target_node.right_child is None or target_node.left_child is None

    def link_node_to_target(self, target_node, added_node):
        """
        Methode to link the child's nodes to searched node
        :param target_node: searched node
        :param added_node: node to be added
        :return:
        """
        if target_node.right_child is None:
            target_node.right_child = added_node
        else:
            target_node.left_child = added_node

    def add_node_on_level(self, target_nodes, added_node):
        """
        Methode to add the child's nodes to searched node on levels
        :param target_nodes: searched node
        :param added_node: node to be added
        :return:
        """
        next_level_nodes = []
        for target_node in target_nodes:
            next_level_nodes += [target_node.right_child, target_node.left_child]
            if target_node is not None and self.node_can_be_added(target_node):
                self.link_node_to_target(target_node, added_node)
                return

        self.add_node_on_level(next_level_nodes, added_node)

    def add_node(self, added_node, target_node):
        """
        Methode to insert node in the tree
        :param added_node: node value
        :param target_node:
        :return:
        """
        self.add_node_on_level([target_node], added_node)

    def find_node(self, data, node):
        """
        Methode to find the node in the binary tree
        :param data:
        :param node:
        :return:
        """
        if node is None:
            return None
        if (node.right_child is not None and node.right_child.data == data) or (
                node.left_child is not None and node.left_child.data == data):
            return node
        left_search = self.find_node(data, node.left_child)
        if left_search is not None:
            return left_search
        return self.find_node(data, node.right_child)

    def find_father(self, data):
        """
        Methode to find the father of the searched node to be deleted
        :param data:
        :return:
        """
        return self.find_node(data, self.root_node)

    def delete_node(self, target_node):
        """
        Methode to delete the target node
        :param target_node: node data
        :return:
        """
        if target_node == self.root_node:
            if target_node.right_child is not None:
                self.root_node = target_node.right_child
            elif target_node.left_child is not None:
                self.root_node = target_node.left_child
            else:
                self.root_node = None

        father = self.find_father(target_node.data)
        if father is None:
            print("NOT FOUND")
            return
        if father.right_child == target_node:
            if target_node.right_child is not None:
                father.right_child = target_node.right_child
            elif target_node.left_child is not None:
                father.right_child = target_node.left_child
            else:
                father.right_child = None

        else:
            # target is left child of father
            if target_node.right_child is not None:
                father.left_child = target_node.right_child
            elif target_node.left_child is not None:
                father.left_child = target_node.left_child
            else:
                father.left_child = None


if __name__ == "__main__":
    n0 = TreeNode('leonardo')
    n1 = TreeNode('l1')
    n2 = TreeNode('l2')
    n3 = TreeNode('chaima')
    # n0.right_child = n1
    # n0.left_child = n2

    # n0.print_TreeNode()

    # print(n0.is_leaf())
    # print(n1.is_leaf())

    arbre = Tree(n0)
    arbre.add_node(n1, n0)
    arbre.add_node(n2, n0)
    arbre.add_node(n3, n1)
    arbre.traversal_deep()
    arbre.delete_node(n0)
    arbre.traversal_deep()
