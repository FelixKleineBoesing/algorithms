#include <string>
#include <iostream>
#include <math.h> /* exp2 */

/* TODO implement own integer class */

class BigInt {
    std::string x;
    public:
        /* BigInt(std::string x = "0"); //constructor */
        /* BigInt operator+(const std::string&)const; // + operators */
        /* short int length(); //length of number */

    BigInt operator+ (BigInt& y) {

        short int len_a = this -> x.length();
        short int len_b = y.length();
        short int iter = std::max(len_a, len_b);
        short int remainder = 0;
        std::string result = "";
        short int c;
        std::string tmp;
        std::string tmp_a;
        std::string tmp_b;

        for (short int i = 0; i < iter; i++) {
            tmp_a = this->x[len_a-1-i];
            tmp_b = y.x[len_b-1-i];
            short int a = std::stoi(tmp_a);
            short int b = std::stoi(tmp_b);
            c = a + b + remainder;
            if (c > 9) {
                remainder = 1;
                tmp = std::to_string(c);
                result = tmp[tmp.length()-1] + result;
            } else {
                result = std::to_string(c) + result;
                remainder = 0;
            }
        }
        if (remainder == 1) {
            result = "1" + result;
        }
        return BigInt(result);
    };

    short int length () {
        short int result;
        return result = x.length();
    };

    BigInt(std::string x) {
    x = x;
    };
};

    int multiply_integers_cpp(std::string int_one, std::string int_two){

        /* init result */
        std::string product;
        std::cout << int_one << std::endl;
        std::cout << int_two << std::endl;

        short int d_one = str_one.length();
        short int d_two = str_two.length();

        if (d_one == 1 or d_two == 1) {
            /* if one is one-digit number than jsut multiply them */
            product = int_one * int_two;
        } else {
            std::cout << "new iteration" << std::endl;
            std::cout << d_one << std::endl;
            std::cout << d_two << std::endl;
            /* fill strings with zeros on the left to get a length which is a power of two */
            short int log_one_int = log(d_one)/log(2);
            float log_one_double = log(d_one)/log(2);

            short int log_two_int = log(d_two)/log(2);
            float log_two_double = log(d_two)/log(2);
            std::cout << log_one_int << std::endl;
            std::cout << log_one_double << std::endl;
            std::cout << log_two_int << std::endl;
            std::cout << log_two_double << std::endl;
            if (log_one_int != log_one_double) {
                short int string_len = exp2(log_one_int + 1);
                str_one = std::string(string_len - d_one, '0') + str_one;
            }

            if (log_two_int != log_two_double) {
                short int string_len = exp2(log_two_int + 1);
                str_two = std::string(string_len - d_two, '0') + str_two;
            }

            std::cout << str_one << std::endl;
            std::cout << str_two << std::endl;
            /*  again get the length of integers */
            d_one = str_one.length();
            d_two = str_two.length();

            /* divide integers in equal parts*/
            BigInt a = std::stoi(str_one.substr(0, d_one / 2));
            BigInt b = std::stoi(str_one.substr(d_one / 2, d_one / 2));

            BigInt c = std::stoi(str_two.substr(0, d_two / 2));
            BigInt d = std::stoi(str_two.substr(d_two / 2, d_two / 2));

            std::cout << a << std::endl;
            std::cout << b << std::endl;
            std::cout << c << std::endl;
            std::cout << d << std::endl;

            /*  apply the four steps of karazuba algorithm*/
            BigInt first_step = multiply_integers_cpp(a, c);
            BigInt second_step = multiply_integers_cpp(b, d);
            BigInt third_step = multiply_integers_cpp(a+b, c+d);
            product = first_step * pow(10, d_one) + (third_step - (second_step + first_step)) * pow(10, d_one / 2) + second_step;
         }
        return product;
    }

#include <stdint.h>
extern "C" {
    char * str multiply_integers_cpp_bar(char * str int_one, char * str int_two) {
        return multiply_integers_cpp(int_one, int_two);
    }
}