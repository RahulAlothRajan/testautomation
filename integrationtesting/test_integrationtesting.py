"""sample test"""
import unittest
from termcolor import colored
import emoji

from integrationtesting import integration_testing

def print_error(string:str):
    text = colored(string, 'red')
    print(text + emoji.emojize(':thumbs_down:'))
    pass
def print_warning(string:str):
    text = colored(string, 'yellow')
    pass
def print_success(string:str):
    text = colored(string, 'yellow')
    pass

class Testintegration_testing(unittest.TestCase):
    """sample test"""

    def test_world(self):
        """sample test"""
        print_error("What the hell")
        self.assertEqual(1, 1)

    def test_world_unicode(self):
        """sample test with unicode"""
        self.assertEqual(2, 2)
