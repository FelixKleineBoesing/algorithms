import math
import clipboard

def count_digits(n):
    if n > 0:
        digits = int(math.log10(n)) + 1
    elif n == 0:
        digits = 1
    else:
        digits = int(math.log10(-n)) + 2
    return digits


def multiply_integers(str_one: str, str_two: str):
    d_one = len(str_one)
    d_two = len(str_two)

    # for lazyness
    #assert d_one == d_two, "must be equal long!"
    # must be power of two
    if d_one == 1 and d_two == 1:
        return int(str_one) * int(str_two)
    if int(math.log2(d_one)) != math.log2(d_one) or d_one < d_two:
        str_one = str_one.zfill(2**(int(math.log2(d_one)) + 1))
    if int(math.log2(d_two)) != math.log2(d_two) or d_two < d_one:
        str_two = str_two.zfill(2**(int(math.log2(d_two)) + 1))
    d_one = len(str_one)
    d_two = len(str_two)
    a, b = str_one[0:int(d_one/2)], str_one[int(d_one/2):d_one]
    c, d = str_two[0:int(d_two/2)], str_two[int(d_two/2):d_two]

    first_step = int(multiply_integers(a, c))
    first_test = int(a) * int(c)
    second_step = int(multiply_integers(b, d))
    second_test = int(b) * int(d)
    third_step = multiply_integers(str(int(a)+int(b)), str(int(c)+int(d)))
    third_test = (int(a) + int(b)) * (int(c) + int(d))
    fourth_step = int(first_step * (10**d_one) + (third_step - (second_step + first_step)) * (10**int(d_one/2)) + \
                      second_step)
    fourth_test = int(str_one) * int(str_two)
    return fourth_step

if __name__=="__main__":
    #print(multiply_integers(1213, 1313))
    x = "3141592653589793238462643383279502884197169399375105820974944592"
    y = "2718281828459045235360287471352662497757247093699959574966967627"
    a = multiply_integers(x, y)
    print(int(a))
    print(int(x)*int(y))
    clipboard.copy(a)