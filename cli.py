import click
from pizza_factory import PizzaSize, Pizza, bake, deliver, pickup


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
    possible_pizzas = Pizza.get_existing_pizza_types()
    if pizza not in [p.name.lower() for p in possible_pizzas]:
        print('You cannot order this pizza. Try another one. '
              'Call for menu to get list of pizzas that are available today.')
        return
    pizza_template = [p for p in possible_pizzas if p.name.lower() == pizza][0]

    possible_pizza_sizes = [e.value for e in PizzaSize]
    if size not in possible_pizza_sizes:
        print(f'Pizza size should be one of '
              f'{", ".join(possible_pizza_sizes)}.')
        print('Try to order pizza of another size.')
        return
    pizza = pizza_template(size=PizzaSize(size))

    bake(pizza)
    if delivery:
        deliver(pizza)
    else:
        pickup(pizza)


@cli.command()
def menu():
    """
    Prints menu.
    """
    for pizza in Pizza.get_existing_pizza_types():
        print(f'- {pizza().dict()}')


if __name__ == '__main__':
    cli()
