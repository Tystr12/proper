from random import randint
from person import Person

def main() -> None:
    length = int(input('How long should the list be? '))
    limit = int(input('What should the maximum size of number be? Not inclusive. '))
    list_of_numbers = generate_list_of_numbers(length, limit)
    print_list(list_of_numbers)
    print_total_of_even_numbers(list_of_numbers)
    print(f'sum of list: {sum_list(list_of_numbers)}')
    print(destroy_list(list_of_numbers))
    punch()
    x = Person("Siri", 14, "Student", "Horse")
    x.print_info()


def alt() -> None:
    # list_input = list(input('input a list'))
    # print_total_of_even_numbers(list_input)
    word = '[5,5,5,5,2,3,4343,4,4]'
    listnr = input_list_maker(word)
    print_list(listnr)
    print(type(listnr[0]))
    print(sum_list(listnr))


def input_list_maker(word: str) -> str:
    """
    takes an input str list and converts it to a list of ints that python can understand

    :param word: list in str from input
    :return: a list of ints
    """
    count = 0
    imp = word.replace(',', '').replace('[', '').replace(']', '')
    list_nums = []
    for i in imp:
        value = int(i)
        list_nums.insert(value, value)
        count = count + 1
    print(list_nums)
    return list_nums


def print_list(list_of_numbers: list) -> None:
    """
    Prints the contents of a list to the terminal.

    :param list_of_numbers: list you want to print out
    :return: None
    """
    for i in list_of_numbers:
        print(i)


def generate_list_of_numbers(length: int, limit: int) -> list:
    """
    Generates a list of random numbers based on the parameters given and returns it.

    :param length: the length of the list you want to generate.
    :param limit: the maximum highest number that can be in the list
    :return: returns a list of random numbers based on the parameters given.
    """
    list_of_numbers = []
    for i in range(int(length)):
        current = randint(1, int(limit))
        list_of_numbers.insert(i, current)
    return list_of_numbers


def print_total_of_even_numbers(list_of_numbers: list) -> None:
    """
    Finds the amount of even numbers in the list and prints the value to the console.

    :param list_of_numbers: the list you want to find the amount of even numbers in.
    :return: the number of even numbers in the list.
    """
    even_numbers = 0
    for number in list_of_numbers:
        if number % 2 == 0:
            even_numbers = even_numbers + 1

    print(f'There are {even_numbers}/{len(list_of_numbers)} even numbers in the list total')


def sum_list(list_of_numbers: list) -> int:
    """
    Sums up all values in a list(int) and returns the result.

    :param list_of_numbers: list of numbers to sum up.
    :return: an int value of summed indexes from list.
    """
    sum_of_list = 0
    for number in list_of_numbers:
        sum_of_list = sum_of_list + number

    return sum_of_list


def destroy_list(list_of_numbers: list) -> None:
    """
    mess with the data of a list without actually messing with the actual list.

    :param list_of_numbers: list of ints
    :return: None, prints the eventual value
    """
    sum_of_list = sum_list(list_of_numbers)
    print(sum_of_list)
    for number in list_of_numbers:
        if list_of_numbers.index(number) % 2 == 0:
            print('-', number)
            sum_of_list = sum_of_list - number
        else:
            print('+', number)
            sum_of_list = sum_of_list + number
        print('sum: ', sum_of_list)


def punch() -> None:
    """
    Prints punch to the terminal.

    :return: None
    """
    print('PUNCH!')


if __name__ == "__main__":
    main()
