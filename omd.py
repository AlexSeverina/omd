# Guido van Rossum <guido@python.org>
import random


def step_3_1_in_bar(num_of_coins, min_number_of_glasses):
    """
    Final part of the story where it is chosen how much will duck drink and how bad she
    will feel tomorrow.

    :param num_of_coins: Number of coins that duck has and can spend on whiskey.
    :param min_number_of_glasses: Minimum number of glasses that duck needs to drink to feel well.
    """
    print('Сколько стаканов виски 🥃 сегодня вместит утячье тельце? 🤔\n'
          f'1 стакан = 1 монетка. У утки {num_of_coins} монеток')
    num_of_glasses_options = [str(x) for x in range(min_number_of_glasses,
                                                    num_of_coins + 1)]
    num_of_glasses = int(force_choose_option(num_of_glasses_options))

    if num_of_glasses == num_of_coins:
        print('Утка пропила все свои деньги и всю следующую неделю жила на подлапном корме. \n'
              'Но вернемся к событиям текущего вечера: ')

    if num_of_glasses > 4:
        print('Утка-маляр 🦆 напилась до беспамятства. \n'
              'Она не помнила, как прошел вечер, но на следующий день \n'
              'во всю стену ее дома была нарисована большая булка. ')
    else:
        print('Утка-маляр 🦆 приятно провела вечер: '
              'она шутила, смеялась и много танцевала. \n'
              'Малярные способности ей сегодня не пригодились. \n'
              'К следующей пятнице она заработает еще монеток и снова придет в бар. ')


def step3_cold_in_bar(num_of_coins, min_number_of_glasses):
    """
    Part of the story where duck gets wet and grumpy.

    :param num_of_coins: Number of coins that duck has.
    :param min_number_of_glasses: Minimum number of glasses that duck needs to drink to feel well.
    """
    min_number_of_glasses += 2
    print('Промокшая, но упорная, утка таки вошла в бар. \n'
          'Ей жизненно необходимо что-то горячительное. ')
    step_3_1_in_bar(num_of_coins, min_number_of_glasses)


def step2_umbrella(num_of_coins, min_number_of_glasses):
    """
    Part of the story where it rains but lucky duck has an umbrella.

    :param num_of_coins: Number of coins that duck has.
    :param min_number_of_glasses: Minimum number of glasses that duck needs to drink to feel well.
    """
    print('Скоро на улице пошел дождь 🌧 и утке пригодился ее зонтик.')

    num_of_found_coins = round(random.random() * 3)
    num_of_coins += num_of_found_coins
    if num_of_found_coins:
        print(f'Довольно шлепая по лужам, утка даже нашла монетки на дороге: {num_of_found_coins}.')

    print('Сверкая сухими перышками и неиспорченной прической, '
          'утка вошла в бар.')
    step_3_1_in_bar(num_of_coins, min_number_of_glasses)


def step2_no_umbrella(num_of_coins, min_number_of_glasses):
    """
    Part of the story where duck decides whether the rain starts and
    duck decides if the bar is really worth it.

    :param num_of_coins: Number of coins that duck has.
    :param min_number_of_glasses: Minimum number of glasses that duck needs to drink to feel well.
    """
    print('Не прошла утка и двух кварталов, как начался дождь. 🌧 \n'
          'Утке вернуться домой?')

    options = {'да': True, 'нет': False}
    if not options[force_choose_option(options)]:
        return step3_cold_in_bar(num_of_coins, min_number_of_glasses)
    return print('Утка-маляр 🦆 грустно и трезво провела вечер дома.')


def force_choose_option(options):
    """
    Function that makes the user choose from the number of option one
    to continue the story.

    :param options: Iterable that contains options to choose from.
    """
    option = ''
    while option not in options:
        print(('Выберите: ' + '{}/' * (len(options) - 1) + '{}').format(*options))
        option = input()
    return option


def step1(num_of_coins, min_number_of_glasses):
    """
    The beginning of the story where duck decides to go to the bar.

    :param num_of_coins: Number of coins that duck has.
    :param min_number_of_glasses: Minimum number of glasses that duck needs to drink to feel well.
    """
    print('Утка-маляр 🦆 решила выпить зайти в бар. '
          f'У нее было целых {num_of_coins} монеток, на которые можно неплохо покутить. '
          'Взять ей зонтик? ☂️')

    options = {'да': True, 'нет': False}
    if options[force_choose_option(options)]:
        return step2_umbrella(num_of_coins, min_number_of_glasses)
    return step2_no_umbrella(num_of_coins, min_number_of_glasses)


if __name__ == '__main__':
    step1(num_of_coins=5, min_number_of_glasses=0)
