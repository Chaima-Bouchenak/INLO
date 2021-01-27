#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A script that creat a Node class
and two attributs to establish the link between nodes
"""


class Node:
    """
    Class representing nodes trough chained list.
    node has two properties: data + pointer of the next node
    """

    def __init__(self, param_data: int):
        """
        Constructor
        param_data: node value
        """
        self.data = param_data
        self.link = None

    def __str__(self):
        """
        Return: a string representation of a node and its link
        """
        nodes_list = []
        node = self

        while node.link is not None:
            nodes_list.append(node.data)
            node = node.link
        nodes_list.append(node.data)
        return str(nodes_list)
