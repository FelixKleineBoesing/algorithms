#include <string>
#include <iostream>
#include <math.h> /* exp2 */

/* TODO implement own integer class */

    int multiply_integers_cpp(long long int int_one, long long int int_two){

        /* init result */
        long long int product;
        std::cout << int_one << std::endl;
        std::cout << int_two << std::endl;

        std::string str_one = std::to_string(int_one);
        std::string str_two = std::to_string(int_two);

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
            long long int a = std::stoi(str_one.substr(0, d_one / 2));
            long long int b = std::stoi(str_one.substr(d_one / 2, d_one / 2));

            long long int c = std::stoi(str_two.substr(0, d_two / 2));
            long long int d = std::stoi(str_two.substr(d_two / 2, d_two / 2));

            std::cout << a << std::endl;
            std::cout << b << std::endl;
            std::cout << c << std::endl;
            std::cout << d << std::endl;

            /*  apply the four steps of karazuba algorithm*/
            long long int first_step = multiply_integers_cpp(a, c);
            long long int second_step = multiply_integers_cpp(b, d);
            long long int third_step = multiply_integers_cpp(a+b, c+d);
            product = first_step * pow(10, d_one) + (third_step - (second_step + first_step)) * pow(10, d_one / 2) + second_step;
         }
        return product;
    }

#include <stdint.h>
extern "C" {
    int32_t multiply_integers_cpp_bar(int32_t int_one,int32_t int_two) {
        return multiply_integers_cpp(int_one, int_two);
    }
}