#include <iostream>
#include <cmath>

int power(int base, int exponent)
{
    double result = 1;
    for (int i = 0; i < exponent; i++;)
    {
        result = result * base;
    }
    return result;
}

int main() {
    int test = power(12, 2);
    std::cout << test << std::endl;
}


























