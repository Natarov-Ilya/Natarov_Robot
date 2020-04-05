#include <iostream>

using namespace std;

int main()
{
    float x, y;
    x = 987654321. * 987654321. - 987654321. * 987654321. + 1.;
    y = 987654321. * 987654321. + 1. - 987654321. * 987654321.;
    cout << x << endl << y << endl;
    return 0;
}
