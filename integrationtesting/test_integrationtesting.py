"""sample test"""
import unittest
import integrationtesting.print_msgs as msg

class Testintegration_testing(unittest.TestCase):
    """sample test"""

    def test_world(self):
        """sample test"""
        msg.print_error("I am printing an error message here:")
        self.assertEqual(1, 2)

    def test_world_unicode(self):
        """sample test with unicode"""
        msg.print_success("I am printing a success  here:")
        self.assertEqual(2, 2)

    def test_world_unicode1(self):
        """sample test with unicode"""
        msg.print_warning("I am printing a warning  here:")
        self.assertEqual(2, 2)