from ctypes import cdll
import os

print(os.getcwd())
lib = cdll.LoadLibrary('./cpp/libMultiplyIntegers.so')


class MultiplyIntegers:
    def __init__(self):
        self.obj = lib.MultiplyIntegers_new()

    def bar(self):
        lib.MultiplyIntegers_bar(self.obj)


if __name__=="__main__":

    f = MultiplyIntegers()
    f.bar()