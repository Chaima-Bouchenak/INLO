import random
import unittest

class RandomTest(unittest.TestCase):
	"""Test case utilisé pour tester les fonctions du module 'random'."""

	def setUp(self):
		"""Initialisation des tests."""
		self.liste = list(range(10))

	def test_choice(self):
		"""Teste le fonctionnement de la fonction 'random.choice'."""
		elt = random.choice(self.liste)
		self.assertIn(elt, self.liste)

	def test_shuffle(self):
		"""Teste le fonctionnement de la fonction 'random.shuffle'."""
		random.shuffle(self.liste)
		self.liste.sort()
		self.assertEqual(self.liste, list(range(10)))

	def test_sample(self):
		"""Teste le fonctionnement de la fonction 'random.sample'."""
		extrait = random.sample(self.liste, 5)
		for element in extrait:
			self.assertIn(element, self.liste)

	def test_sample_check_exception(self):
		"""Teste le fonctionnement de la fonction 'random.sample' dans 
			un cas d'appel incorrect
		"""
		with self.assertRaises(ValueError):
			random.sample(self.liste, 20)


	def test_sample_check_exception2(self):
		"""Teste le fonctionnement de la fonction 'random.sample' dans 
			un cas d'appel incorrect, seconde version
		"""
		self.assertRaises(ValueError, random.sample, self.liste, 20)


	def tearDown(self):
		"""Libération des ressources, fermeture des fichiers eventuellement ouverts dans setUp."""

	def test_choice_erroneous_test(self):
		"""Teste très mal le fonctionnement de la fonction 'random.choice'."""
		elt = random.choice(self.liste)
		self.assertIn(elt, ('a', 'b', 'c'))

	def test_crashing_test(self):
		"""Teste et crashe sur une division par zéro."""
		self.assertEqual(6, 6 / 0)

# Il y'a deux manieres de teste un code et lever une exception :

# ERROR : crash : probleme dans le code
# FAIL : le code s'execute entierement mais le probleme vient de
# la partie de la verification de la condition d'insertion

