#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A script t orepresent a chained list of nodes
"""
from node import Node


class ChainedList:
    """
    Class creating methods to perform actions on a chained lists
    of node objects
    """

    def __init__(self, list_nodes):
        """
        Methode establishing the chained list, by
        creating a list of nodes objects of integer.

        @list_nodes : list tp be transformed to a chained list of Node objects
        """

        self.starter_node = Node(list_nodes[0])
        current_node = self.starter_node
        for val in list_nodes[1:]:
            current_node.link = Node(val)
            current_node = current_node.link

    def __str__(self):
        """
        Return a string representation of the object
        """
        return str(self.starter_node)

    def inser_node_after(self, data_chosen: int, new_node: int):
        """
        Insert a new node with the data in a chained list after the searched data node.

        @data_chosen : searched data
        @new_node : node to insert
        """
        current_node = self.starter_node
        while current_node is not None:  # search the index of the node for the searched data
            if current_node.data == data_chosen:
                break
            current_node = current_node.link

        new_data = Node(new_node)
        new_data.link = current_node.link  # The link for the new node takes the link of the current node
        current_node.link = new_data   # The link for the current node takes the data of the new node

    def delete_node(self, data_chosen):
        """
        Delete nodes whom the value equal to data_chosen

        @data_chosen : searched data to delete
        """

        node_del = self.starter_node

        if node_del is None:
            print("No node to be deleted")

        while node_del is not None:
            if node_del.data == data_chosen:
                node_del.link = node_del.limk.link
            node_del = node_del.link
