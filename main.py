import logging
import os
import argparse
import json
import functools
from random import randint

log = logging.getLogger("application")
hdlr = logging.FileHandler(os.getcwd() + "\\logs.txt")
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
hdlr.setFormatter(formatter)
log.addHandler(hdlr)
log.setLevel(logging.INFO)


def log_info(func):
    def wrapper(*args, **kwargs):
        log.info("Entering {:s}...".format(func.__name__))
        return func(*args, **kwargs)

    return wrapper


@log_info
def sort_by_second_word_list(arg_list):
    arg_list.sort(key=lambda s: s.split()[1])
    return arg_list


@log_info
def sort_by_second_word_dict(dictionary):
    return dict(sorted(dictionary.items(), key=lambda x: x[0].split(" ")[1]))


@log_info
def sort_dictionary_by_values(dictionary):
    return sorted(dictionary.items(), key=lambda x: x[1])


def generate_numbers(x):
    for j in range(x):
        yield j


@log_info
def get_unique_elements():
    # print unique elements from string
    napis = "aabsidddjeifoskdnfeignfkslfkdi"
    unique_elements = list(set(napis))
    # reversed
    return "".join(reversed(unique_elements))


def open_file():
    of = open("people.txt", "a")
    parser = argparse.ArgumentParser(description='Get people into the file.')
    parser.add_argument('--name', metavar='--n', nargs='+',
                        help='Person\'s firstname')

    parser.add_argument('--age', metavar='--a', nargs='+',
                        help='Person\'s age')

    args = parser.parse_args()
    people = {}

    # Merge into dictionary
    for num, name in enumerate(args.name, start=0):
        try:
            people[name] = args.age[num]
        except IndexError:
            log.error("Please check the arguments to have the same amount for names and ages")

    log.info(sort_by_second_word_dict(people))
    log.info(sort_dictionary_by_values)

    of.write(json.dumps(sort_by_second_word_dict(people)))


def sum_by_reduce(list_to_sum):
    return functools.reduce(lambda a, b: a + b, list_to_sum)


@log_info
def example():
    print("Example")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    example_list = ["James Nowak", "Patryk Kowalski", "Michał Wiśniewski"]

    example_dict = {'carl bob': 40,
                    'alan danny': 2,
                    'bob carl': 1,
                    'danny alan': 3}

    print("SORT LIST BY SECOND ELEMENT")
    print(sort_by_second_word_list(example_list))
    print("=============================")

    print("SORT DICT BY SECOND ELEMENT OF KEY")
    print(sort_by_second_word_dict(example_dict))
    print("=============================")

    print("LOGGING DECORATOR")
    example()
    print("=============================")

    print("CREATE LIST FROM GENERATOR")
    generator = generate_numbers(5)
    int_list = []
    for i in generator:
        int_list.append(i)
    print(int_list)
    print("=============================")

    print("OPEN AND WRITE TO A FILE")
    print("PLEASE CHECK LOGS AND PEOPLE.TXT FILE")
    open_file()
    print("=================================")
    print("SUM BY REDUCE")
    lis = [3, 5, 6, 3, 6]
    sum_by_reduce(lis)
    print("=================================")

    print([[".".join("{}".format(randint(0, 255)) for x in range(4))]for i in range(4)])

# dodać do bazy pierwsze zadanie
# echo server, ingormacje do logow przez commandline przyjime cyfry i wykona sumowanie przez reduce,
# wysyła json do clienta
# oblicza minimum i maximum i tez z nimi wysyla json, pokazuje unikalne liczby. Użyć logging, click, multiprocessing

