#include <iostream>
#include <cmath>
int main(){
    
    double temp;
    char unit;

    std::cout << "******* Temperature Converter *******\n";

    std::cout << "What units would you like to convert to: ";
    std::cin >> unit;

    if(unit == 'f' || unit == 'F'){
        std::cout << "Enter temp in Celcius: ";
        std::cin >> temp;
        temp = (temp * (double)9/5) + 32;
        std::cout << temp << " Fahrenheit\n";
    } 

    else if(unit == 'c' || unit == 'C'){
        std::cout << "Enter temp in Fahrenheit: ";
        std::cin >> temp;
        temp = (temp - 32) * ((double)5/9);
        std::cout << temp << " Celcius\n";
    }   
    else{
        std::cout << "Please enter the correct units. (F or C)\n";
    }

    std::cout << "*************************************\n";
    return 0;
}