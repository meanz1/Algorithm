#include <iostream>
#include <stdio.h>

int f[29] = {
    0,
};

int a = 0;
int b = 0;

int fib(int n)
{
    if (n == 1 || n == 2)
    {
        return 1;
    }

    else
    {
        return fib(n - 1) + fib(n - 2);
    }
}

int fibonacci(int n)
{
    f[1] = f[2] = 1;
    for (int i = 3; i <= n; i++)
    {
        f[i] = f[i - 1] + f[i - 2];
        b++;
    }
    return f[n];
}

int main()
{
    int n;
    std::cin >> n;
    std::cout << fibonacci(n) << " " << b << std::endl;
    return 0;
}
