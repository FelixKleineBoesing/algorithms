import math
import clipboard
from ctypes import cdll

lib = cdll.LoadLibrary("algorithms/cpp/libMultiplyIntegers.so")


def multiply_integers_cpp(int_one: int, int_two: int):
    raise NotImplementedError
    return lib.multiply_integers_cpp_bar(int_one, int_two)


def multiply_integers(str_one: str, str_two: str):
    assert isinstance(str_one, str), "str_one must be of type str"
    assert isinstance(str_two, str), "str_two must be of type str"
    '''
    :param str_one: str - integer as type str
    :param str_two: str - integer as type str
    :return: int - product of both input integers
    '''
    d_one = len(str_one)
    d_two = len(str_two)

    # if both numbers have length one than there is no need to applay multiply_integers again
    if d_one == 1 and d_two == 1:
        return int(str_one) * int(str_two)
    # fill strings with zeros on the left to get a length which is a power of two
    if int(math.log2(d_one)) != math.log2(d_one) or d_one < d_two:
        str_one = str_one.zfill(2**(int(math.log2(d_one)) + 1))
    if int(math.log2(d_two)) != math.log2(d_two) or d_two < d_one:
        str_two = str_two.zfill(2**(int(math.log2(d_two)) + 1))

    # again get the length of integers
    d_one = len(str_one)
    d_two = len(str_two)

    #divide integers in equal parts
    a, b = str_one[0:int(d_one/2)], str_one[int(d_one/2):d_one]
    c, d = str_two[0:int(d_two/2)], str_two[int(d_two/2):d_two]

    # apply the four steps of karazuba algorithm
    first_step = int(multiply_integers(a, c))
    second_step = int(multiply_integers(b, d))
    third_step = multiply_integers(str(int(a)+int(b)), str(int(c)+int(d)))
    fourth_step = int(first_step * (10**d_one) + (third_step - (second_step + first_step)) * (10**int(d_one/2)) + \
                      second_step)
    return fourth_step


if __name__=="__main__":
    x = "3141592653589793238462643383279502884197169399375105820974944592"
    y = "2718281828459045235360287471352662497757247093699959574966967627"
    a = multiply_integers(x, y)
    print(int(a))
    print(int(x)*int(y))
    clipboard.copy(a)