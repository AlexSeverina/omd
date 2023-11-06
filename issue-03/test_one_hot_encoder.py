from one_hot_encoder import fit_transform
import unittest


class TestFitTransform(unittest.TestCase):
    """
    Test class for fit_transform function.
    """

    def test_empty(self):
        """
        Test with empty (invalid) input.
        """
        self.assertRaises(TypeError, fit_transform)

    def test_one_string(self):
        """
        Test with input consisting of one string.
        """
        actual = fit_transform('one')
        expected = [('one', [1])]
        self.assertEqual(actual, expected)

    def test_type(self):
        """
        Test for inspecting the type of the output.
        """
        actual = fit_transform('the', 'nut', 'cracker')
        self.assertIsInstance(actual, list)

    def test_multiple_strings(self):
        """
        Test with multistring input.
        """
        actual = fit_transform(['dog', 'goes', 'woof',
                                'cat', 'goes', 'meow'])
        self.assertEqual(actual,
                         [('dog', [0, 0, 0, 0, 1]),
                          ('goes', [0, 0, 0, 1, 0]),
                          ('woof', [0, 0, 1, 0, 0]),
                          ('cat', [0, 1, 0, 0, 0]),
                          ('goes', [0, 0, 0, 1, 0]),
                          ('meow', [1, 0, 0, 0, 0])])
