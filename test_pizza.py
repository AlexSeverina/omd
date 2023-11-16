import unittest
from pizza_factory import \
    PizzaSize, Pepperoni, Margherita, Hawaiian
from cli import menu, order
from unittest.mock import patch
from click.testing import CliRunner


class TestPizza(unittest.TestCase):
    """
    Test class for Pizza class.
    """

    def test_size_assignment(self):
        """
        Test that creating pizza with wrong size does not work.
        """
        with self.assertRaises(ValueError):
            Margherita(size=PizzaSize('XXL'))

    def test_equal(self):
        """
        Test for __eq__ method with equal pizzas.
        """
        assert Pepperoni(size=PizzaSize('XL')) == \
               Pepperoni(size=PizzaSize('XL'))

    def test_not_equal(self):
        """
        Test for __eq__ method with different pizzas.
        """
        assert Hawaiian(size=PizzaSize('XL')) != \
               Hawaiian(size=PizzaSize('L'))

    def test_correct_dict(self):
        """
        Test that dict is created correctly.
        """
        assert Margherita().dict() == \
               'Margherita 🧀: tomato sauce, mozzarella, tomatoes'


class TestOrder(unittest.TestCase):
    """
    Test class for order function.
    """

    def test_wrong_pizza(self):
        """
        Test order output for wrong pizza.
        """
        runner = CliRunner()
        result = runner.invoke(order, 'neapolitan'.split())
        assert result.output == \
            'You cannot order this pizza. Try another one.' \
            'Call for menu to get list of pizzas that are available today.\n'

    def test_wrong_pizza_size(self):
        """
        Test order output for wrong pizza size.
        """
        runner = CliRunner()
        result = runner.invoke(order, 'pepperoni --size S'.split())
        assert result.output == \
            'Pizza size should be one of L, XL.\n' \
            'Try to order pizza of another size.\n'

    @patch('random.randint')
    def test_order_without_flags(self, randint_mock):
        """
        Test order creates L pizza for pick up.
        """
        randint_mock.return_value = 1
        runner = CliRunner()
        result = runner.invoke(order, 'hawaiian'.split())
        assert result.output == \
            'Making delicious L hawaiian pizza...\n' \
            '🔥 Baked in 1s!\n' \
            'Waiting for the pick up for L hawaiian pizza...\n' \
            '🏠 Picked up in 1s!\n'

    @patch('random.randint')
    def test_order_with_delivery(self, randint_mock):
        """
        Test order creates L pizza for delivery.
        """
        randint_mock.return_value = 1
        runner = CliRunner()
        result = runner.invoke(order, 'pepperoni --delivery')
        assert result.output == \
            'Making delicious L pepperoni pizza...\n' \
            '🔥 Baked in 1s!\n' \
            'Deliver L pepperoni pizza to the address...\n' \
            '🛵 Delivered in 1s!\n'

    @patch('random.randint')
    def test_order_with_delivery_and_size(self, randint_mock):
        """
        Test order creates XL pizza for delivery.
        """
        randint_mock.return_value = 1
        runner = CliRunner()
        result = runner.invoke(order, 'margherita --delivery --size XL')
        assert result.output == \
               'Making delicious XL margherita pizza...\n' \
               '🔥 Baked in 1s!\n' \
               'Deliver XL margherita pizza to the address...\n' \
               '🛵 Delivered in 1s!\n'


class TestMenu(unittest.TestCase):
    def test_prints(self):
        """
        Test for one call of menu.
        """
        runner = CliRunner()
        result = runner.invoke(menu)
        assert result.output == \
               '- Margherita 🧀: tomato sauce, mozzarella, tomatoes\n' \
               '- Pepperoni 🍕: tomato sauce, mozzarella, pepperoni\n' \
               '- Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapples\n'
