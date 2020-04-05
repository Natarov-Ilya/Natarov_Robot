#include <iostream>

using namespace std;

void print_binary_int(unsigned int N);

int main()
{
    unsigned int N;
    cin >> N;
    print_binary_int(N);
    return 0;
}

void print_binary_int (unsigned int N)
{
    int* c = new int[32];
    for (int i = 0; i < 32; i ++)
    {
        c[i] = N % 2;
        N = N / 2;
    }
    for (int i = 31; i >= 0; i --)
    {
        cout << c[i];
        if (i % 8 == 0)
        {
            cout << " ";
        }
    }
}
