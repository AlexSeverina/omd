import random
import enum
from typing import Callable


class PizzaSize(enum.Enum):
    """
    Possible pizza sizes.
    """
    BigSize = 'L'
    TheBiggestSize = 'XL'


class Pizza:
    """
    Class for any kind of pizza.
    Each pizza has its name, icon, recipe and size that should
    be one of possible PizzaSizes.
    """
    def __init__(self,
                 name: str,
                 icon: str,
                 recipe: list,
                 size: PizzaSize = PizzaSize.BigSize):
        self.name = name
        self.icon = icon
        self.recipe = recipe
        self.size = size

    def __eq__(self, other):
        """
        Compares current pizza with other pizza.
        All the parameters should be the same.

        :param other: other pizza instance
        :return: if pizzas are identical
        """
        return self.dict() == other.dict() and self.size == other.size

    def dict(self):
        """
        Creates description of a pizza kind.

        :return: dict-like string description with recipe
        """
        return f'{self.name} {self.icon}: {", ".join(self.recipe)}'

    @classmethod
    def get_existing_pizza_types(cls):
        return cls.__subclasses__()


class Margherita(Pizza):
    """
    Margherita pizza class.
    """

    name = 'Margherita'
    icon = '🧀'
    recipe = ['tomato sauce', 'mozzarella', 'tomatoes']

    def __init__(self, size: PizzaSize = PizzaSize.BigSize):
        super().__init__(self.name, self.icon, self.recipe, size)


class Pepperoni(Pizza):
    """
    Pepperoni pizza class.
    """

    name = 'Pepperoni'
    icon = '🍕'
    recipe = ['tomato sauce', 'mozzarella', 'pepperoni']

    def __init__(self, size: PizzaSize = PizzaSize.BigSize):
        super().__init__(self.name, self.icon, self.recipe, size)


class Hawaiian(Pizza):
    """
    Hawaiian pizza class.
    """

    name = 'Hawaiian'
    icon = '🍍'
    recipe = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']

    def __init__(self, size: PizzaSize = PizzaSize.BigSize):
        super().__init__(self.name, self.icon, self.recipe, size)


def log(str_arg: str) -> Callable:
    """Decorator factory that creates decorator for the given str_arg."""
    def decorator(function) -> Callable:
        """Decorator that creates wrapper."""
        def wrapper(*args, **kwargs):
            """
            Wrapper that prints the given str_arg formatted with random
            integer number after the call of the function.
            """
            result = function(*args, **kwargs)
            r = random.randint(1, 10)
            print(str_arg.format(r))
            return result

        return wrapper

    return decorator


@log('🔥 Baked in {}s!')
def bake(pizza):
    """Bakes pizza."""
    print(f'Making delicious {pizza.size.value} {pizza.name.lower()} pizza...')


@log('🛵 Delivered in {}s!')
def deliver(pizza):
    """Delivers pizza."""
    print(f'Deliver {pizza.size.value} {pizza.name.lower()} '
          f'pizza to the address...')


@log('🏠 Picked up in {}s!')
def pickup(pizza):
    """Waits for pick up."""
    print(f'Waiting for the pick up for {pizza.size.value} '
          f'{pizza.name.lower()} pizza...')


if __name__ == '__main__':
    print(Pepperoni().dict())
