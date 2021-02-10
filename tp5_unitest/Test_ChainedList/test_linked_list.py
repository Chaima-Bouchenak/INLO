"""
Script pour tester la classe de la liste chainee
PS : pylint 10/10 8)
"""

import unittest
from linkedList import Node, LinkedList


class TestChainedList(unittest.TestCase):
    """Test case utilisé pour tester les methodes de liste chainee."""

    def setUp(self):
        """Initialisation des tests."""
        self.liste = LinkedList(["a", "b", "c", "d", "e"])
        self.liste_new = LinkedList([])

    def test_new_list_is_empty(self):
        """Tester qu'une liste chainee venant d’être créée est vide"""
        self.assertIsNone(self.liste_new.head)

    def test_not_empty_after_add_elem(self):
        """Tester qu'une liste chainee sur laquelle on vient d’empiler un élément est non vide"""
        self.liste_new.add_first(Node("r"))
        assert (self.liste_new.head) is not None

    def test_empiled_depiled_list_unchanged(self):
        """Tester qu'une 3. une liste chainee qui subit un empilement
        suivi d’un dépilement est inchangée"""
        #liste1 = LinkedList(["a", "b", "c", "d", "e"])
        liste2 = LinkedList(["a", "b", "c", "d", "e"])
        liste2.add_last(Node("f"))
        liste2.remove_node("f")

        node1 = self.liste.head
        node2 = liste2.head

        if node1 is None and node2 is None:
            return True

        while node1 is not None and node2 is not None:
            assert node1.data == node2.data
            node1 = node1.next
            node2 = node2.next

        assert (node1) is None and (node2) is None

    def test_top_element_first(self):
        """Tester que le sommet d’une liste chainee sur laquelle on vient
        d’empiler au debut un élément e est e."""
        node_added_on_top = Node("e")
        self.liste.add_first(node_added_on_top)
        self.assertEqual(str(self.liste.get(0)),"e")

    def test_top_element_last(self):
        """Tester que le sommet d’une liste chainee sur laquelle on vient
        d’empiler a la fin un élément e est e."""
        node_added_on_top = Node("e")
        self.liste.add_last(node_added_on_top)

        node1 = self.liste.head
        while node1 is not None and node1.next is not None:
            node1 = node1.next

        assert node1 == node_added_on_top

    def tearDown(self):
        """Libération des ressources, fermeture des fichiers eventuellement ouverts dans setUp."""


if __name__ == '__main__':
    unittest.main()
