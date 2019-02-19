
#include <iostream>

class MultiplyIntegers{
    public:
        void bar(){
            std::cout << "Hello" << std::endl;
        }
};


extern "C" {
    MultiplyIntegers* MultiplyIntegers_new(){ return new MultiplyIntegers(); }
    void MultiplyIntegers_bar(MultiplyIntegers* foo){ foo->bar(); }
}