import os
print(os.getcwd())
from ctypes import cdll
lib = cdll.LoadLibrary('src/foo/libfoo.so')

class Foo:
    def __init__(self):
        self.obj = lib.Foo_new()

    def bar(self):
        lib.Foo_bar(self.obj)


if __name__=="__main__":
    f = Foo()
    f.bar()