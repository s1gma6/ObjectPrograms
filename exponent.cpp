# include <iostream>
//namespaces
using std::cout;
using std::cin;
using std::endl;

int power(int base, int exponent) {
    int result = 1;
    for (int i=0; i < exponent; i++) {
        result = result * base;
    }
    return result;
}
int main() {
    int x;
    int y;
    cout << "Base number" << endl;
    cin >> x;
    cout << "Exponent number" << endl;
    cin >> y;
    cout << power(x, y) << endl;
    printf("FUCKING RETARDED LANGUAGE");
}