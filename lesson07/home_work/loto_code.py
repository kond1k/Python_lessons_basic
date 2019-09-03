import random


def init_numbers():
    return [num for num in range(1, 91)]


def get_random_numbers_for_row():
    numbers_for_random = [i for i in range(9)]
    [numbers_for_random.remove(random.choice(numbers_for_random)) for _ in range(4)]
    return numbers_for_random


def get_random_nums(nums):
    my_nums = []
    for i in range(5):
        num_for_remove = random.choice(nums)
        nums.remove(num_for_remove)
        my_nums.append(num_for_remove)
    return sorted(my_nums)


def check_number(card, number):
    for i in range(len(card)):
        for j in range(len(card[i])):
            if card[i][j] == number:
                card[i][j] = '--'
                return True
    return False


def init_card():
    card = [['  '] * 9 for _ in range(3)]
    all_numbers = init_numbers()
    for i in card:
        count = 0
        rand_num_for_row = get_random_numbers_for_row()
        rand_num = get_random_nums(all_numbers)
        for j in rand_num_for_row:
            i[j] = rand_num.pop(0)
    return card


def print_card(my, comp):
    print('---------------Ваша карточка----------------')
    for i in my:
        print(i)
    print('------------Карточка компьютера-------------')
    for i in comp:
        print(i)


def check_win(card):
    a = [[j for j in i if type(j) == int] for i in card]
    if len(a[0]) == 0 and len(a[1]) == 0 and len(a[2]) == 0:
        return False
    return True


my_card = init_card()
comp_card = init_card()
all_numbers = init_numbers()
while True:
    print_card(my_card, comp_card)
    selected_num = random.choice(all_numbers)
    print(f'Выпал бочонок с номером {selected_num}')
    answer = input('Желаете зачеркнуть или продолжить ? \n')
    all_numbers.remove(selected_num)
    correct = check_number(my_card, selected_num)
    check_number(comp_card, selected_num)
    if answer == 'зачеркнуть' and not correct:
        print('Такой цифры нет в вашей карточке, вы проиграли')
        break
    if answer == 'продолжить' and correct:
        print('Такая цифра есть в вашей карточке, вы проиграли')
        break
    if not check_win(my_card):
        print('Поздравляю вы выиграли!')
        break
    if not check_win(comp_card):
        print('Компютер зачеркнул все цифры, вы проиграли!')
        break
