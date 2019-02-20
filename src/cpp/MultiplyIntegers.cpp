#include <string>
#include <iostream>
#include <math.h> /* exp2 */

    int multiply_integers_cpp(int int_one, int int_two){

        /* init result */
        int product;
        std::string str_one = std::to_string(int_one);
        std::string str_two = std::to_string(int_two);

        int d_one = str_one.length();
        int d_two = str_two.length();

        if (d_one == 1 and d_two == 1) {
            product = int_one * int_two;
        } else {
            /* fill strings with zeros on the left to get a length which is a power of two */
            int log_one_int = log(d_one)/log(2);
            double log_one_double = log(d_one)/log(2);

            int log_two_int = log(d_two)/log(2);
            double log_two_double = log(d_two)/log(2);

            if (log_one_int != log_one_double or d_one < d_two) {
                int string_len = exp2(d_one + 1);
                str_one = std::string(string_len - d_one, '0') + str_one;
            }
            if (log_two_int != log_two_double or d_two < d_one) {
                int string_len = exp2(d_two + 1);
                str_two = std::string(string_len - d_two, '0') + str_two;
            }
            /*  again get the length of integers */
            d_one = str_one.length();
            d_two = str_two.length();

            /* divide integers in equal parts*/
            int a = std::stoi(str_one.substr(0, d_one/2));
            int b = std::stoi(str_one.substr(d_one/2, d_one/2));

            int c = std::stoi(str_two.substr(0, d_two/2));
            int d = std::stoi(str_two.substr(d_two/2, d_two/2));

            /*  apply the four steps of karazuba algorithm*/
            int first_step = multiply_integers_cpp(a, c);
            int second_step = multiply_integers_cpp(b, d);
            int third_step = multiply_integers_cpp(a+b, c+d);
            product = first_step * pow(10, d_one) + (third_step - (second_step + first_step)) * pow(10, d_one/2) + second_step;
         }
        return product;
    }


extern "C" {
    int multiply_integers_cpp_bar(int int_one, int int_two){return multiply_integers_cpp(int_one, int_two);}
}