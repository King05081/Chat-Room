#include <iostream>
#include <vector>
#include <cmath>

typedef std::vector<std::pair<std::string, int>> pairlist_t;

namespace first{
    int x = 1;
}

namespace second{
    int x = 2;
}

int main(){
    
    double a;
    double b; 
    double c;

    std::cout << "What is the value of a? ";
    std::cin >> a;

    std::cout << "What is the value of b? ";
    std::cin >> b;

    
    a = pow(a, 2);
    b = pow(b, 2);
    c = sqrt((a + b));


    std::cout << c;
    return 0;
}