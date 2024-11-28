#include <iostream>
#include <cmath>

int main(){

    char op;
    double num1;
    double num2;
    double result;

    std::cout << "************** CALCULATOR **************\n";

    std::cout << "Enter number one: ";
    std::cin >> num1;

    std::cout << "Enter either (+ - * /): ";
    std::cin >> op;

    std::cout << "Enter number two: ";
    std::cin >> num2;

    switch(op){
        case '+':
            result = num1 + num2;
            std::cout << "Answer: " << result << '\n';
            break;

            case '-':
            result = num1 - num2;
            std::cout << "Answer: " << result << '\n';
            break;

            case '*':
            result = num1 * num2;
            std::cout << "Answer: " << result << '\n';
            break;

            case '/':
            result = num1 / num2;
            std::cout << "Answer: " << result << '\n';
            break;

            default: 
            std::cout << "Please enter the correct sign (+ - * /).\n";
            break;
    }

    std::cout << "****************************************";

    return 0;
}