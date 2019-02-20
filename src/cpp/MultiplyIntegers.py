from ctypes import cdll
import os

print(os.getcwd())
lib = cdll.LoadLibrary("src/cpp/libMultiplyIntegers.so")

def multiply_integers_cpp(int_one: int, int_two: int):
    return lib.multiply_integers_cpp_bar(int_one, int_two)


if __name__=="__main__":

    f = multiply_integers_cpp(12088748408453754, 884357530358578560)
    print(f)
