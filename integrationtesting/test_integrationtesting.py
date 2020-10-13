"""sample test"""
import unittest
import integrationtesting.print_msgs as msg
import matplotlib.pyplot as plt

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
        # Create data
        N = 500
        x = np.random.rand(N)
        y = np.random.rand(N)
        colors = (0,0,0)
        area = np.pi*3
        plt.scatter(x, y, s=area, c=colors, alpha=0.5)
        plt.title('Scatter plot pythonspot.com')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show(block=True)
        msg.print_warning("I am printing a warning  here:")
        self.assertEqual(2, 2)
