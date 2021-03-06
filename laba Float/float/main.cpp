#include <iostream>

using namespace std;

void print_binary_int(unsigned int N);
void print_binary_float (float N);

int main()
{
    float N;
    cin >> N;
    print_binary_float(N);
    return 0;
}

void print_binary_float(float N)
{
    unsigned int* M = (unsigned int*) &N;
    print_binary_int(*M);
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
