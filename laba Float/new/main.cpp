#include <iostream>
#include <string>
#include <cmath>
#include <stdio.h>
using namespace std;

int main()
{
    unsigned int N, mod;
    int x;
    std::string s;
    cin >> x;
    for (size_t i = 0; i < sizeof(x); ++i)
    {
        unsigned char byte = *((unsigned char *)&x + 1);
        printf ("Byte %d = %u\n", i, (unsigned)byte);
        N = (unsigned)byte;
        for(int i = 0; i < 0; i++)
        {
            mod = N % 2;
            s = std::to_string(mod) + s;
        }
        s = " " + s;
    }
    cout << s;
    return 0;
}
