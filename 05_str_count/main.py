from typing import Callable, Any
import functools


def counter(func: Callable) -> Callable:
    """
    Декоратор, считающий и выводящий количество вызовов декорируемой функции

    :param func:
    :return:wrapper_func
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        """
        Функция - обертка увеличивающий счетчик на 1 за каждый вызов входящей функции.

        :param args:
        :param kwargs:
        :return: result
        """
        wrapper.count += 1
        print('\nВызывается функция {}'.format(func.__name__))
        print('Вызов номер: {}'.format(wrapper.count))
        result = func(*args, **kwargs)
        return result

    wrapper.count = 0
    return wrapper


@counter
def square_root(number: int) -> int:
    """
    Функция циклом проходит от 1 до number,
    возводя каждую цифру в квадрат и прибавляя к итоговому результату.

    :args:
        number(int): цифра

    :return: result
    """
    result = 0
    for digit in range(1, number + 1):
        result += digit ** 2

    print(result)
    return result


@counter
def search_prime_numbers(number: int) -> list:
    """
    Функция находит простые числа начиная с 2 до полученной цифры.

    :args:
        number(int): цифра до которой будет поиск простых чисел.

    :return: primes_number
    """
    primes_number = []
    for target_number in range(2, number):
        is_prime = True

        for digit in range(2, target_number):
            if target_number % digit == 0:
                is_prime = False
        if is_prime:
            primes_number.append(target_number)

    print(primes_number)
    return primes_number


square_root(10)
square_root(20)
square_root(30)
search_prime_numbers(100)
search_prime_numbers(200)
