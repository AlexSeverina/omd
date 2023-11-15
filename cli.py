import click
import pizza_factory
from pizza_factory import PizzaSize, Pizza, bake, deliver, pickup
import inspect


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.option('--size', default=PizzaSize.BigSize.value)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool, size: str):
    """
    Prepares and delivers pizza.

    :param pizza: name of pizza to prepare
    :param delivery: flag to distinguish delivery from pick up
    :param size: size of pizza
    """
    possible_pizzas = get_menu()

    if pizza not in [p.name.lower() for p in possible_pizzas]:
        print('You cannot order this pizza. Try another one. '
              'Call for menu to get list of pizzas that are available today.')
        return
    cur_pizza = [p for p in possible_pizzas if p.name.lower() == pizza][0]

    possible_pizza_sizes = [e.value for e in PizzaSize]
    if size not in possible_pizza_sizes:
        print(f'Pizza size should be one of '
              f'{", ".join(possible_pizza_sizes)}.')
        print('Try to order pizza of another size.')
        return
    cur_pizza.set_size(size=PizzaSize(size))

    bake(cur_pizza)
    if delivery:
        deliver(cur_pizza)
    else:
        pickup(cur_pizza)


@cli.command()
def menu():
    """
    Prints menu.
    """
    for pizza in get_menu():
        print(f'- {pizza.dict()}')


def get_menu() -> list:
    """
    Creates list of pizzas from the menu.
    All pizza-children from Pizza class are included.

    :return: list of pizzas
    """
    pizza_list = list()
    for name, obj in inspect.getmembers(pizza_factory):
        if hasattr(obj, "__bases__") and Pizza in obj.__bases__:
            pizza_list.append(obj())
    return pizza_list


if __name__ == '__main__':
    cli()
