#include <iostream>
#include <stack>
#include <string>

int main()
{
    int n;
    std::cin >> n;
    std::stack<int> stack;

    for (int i = 0; i < n; i++)
    {
        std::string order;
        std::cin >> order;

        if (order == "top")
        {
            if (stack.empty() == 1)
                std::cout << -1 << std::endl;
            else
                std::cout << stack.top() << std::endl;
        }
        else if (order == "size")
            std::cout << stack.size() << std::endl;
        else if (order == "empty")
            std::cout << stack.empty() << std::endl;
        else if (order == "pop")
        {
            if (stack.empty() == 1)
                std::cout << -1 << std::endl;
            else
            {
                std::cout << stack.top() << std::endl;
                stack.pop();
            }
        }
        else if (order == "push")
        {
            int push_n;
            std::cin >> push_n;

            stack.push(push_n);
        }
        else
            return -1;
    }
    return 0;
}