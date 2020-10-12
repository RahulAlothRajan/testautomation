"""sample test"""
import unittest

from integrationtesting import integration_testing


class Testintegration_testing(unittest.TestCase):
    """sample test"""

    def test_world(self):
        """sample test"""
        self.assertEqual(1, 1)

    def test_world_unicode(self):
        """sample test with unicode"""
        self.assertEqual(2, 2)
