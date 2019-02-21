from ctypes import cdll
import os

print(os.getcwd())
lib = cdll.LoadLibrary("src/cpp/libMultiplyIntegers.so")

def multiply_integers_cpp(int_one: int, int_two: int):
    return lib.multiply_integers_cpp_bar(int_one, int_two)


if __name__=="__main__":

    int_one = int(1e4)
    int_two = int(1e4)
    f = multiply_integers_cpp(int_one, int_two)
    g = int_one * int_two
    print(f == g)
    print(f)
    print(g)
