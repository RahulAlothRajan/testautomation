"""sample test"""
import unittest

from integrationtesting import integration_testing


class Testintegration_testing(unittest.TestCase):
    """sample test"""

    def test_world(self):
        """sample test"""
        self.assertEqual(hello('world'), 'hello world')

    def test_world_unicode(self):
        """sample test with unicode"""
        self.assertEqual(hello(u'world'), u'hello world')