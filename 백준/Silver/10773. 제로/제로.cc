#include <iostream>
#include <stack>

int main()
{
    int n;
    std::cin >> n;
    std::stack<int> stack;

    for (int i = 0; i < n; i++)
    {
        int s_in;
        std::cin >> s_in;

        if (s_in != 0)
        {
            stack.push(s_in);
        }
        else if (s_in == 0)
        {
            stack.pop();
        }
    }
    int sum = 0;
    int s_size = stack.size();
    for (int i = 0; i < s_size; i++)
    {
        sum += stack.top();
        stack.pop();
    }

    std::cout << sum << std::endl;
    return 0;
}