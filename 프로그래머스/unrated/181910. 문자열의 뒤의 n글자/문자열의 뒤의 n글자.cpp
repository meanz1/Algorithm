#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string solution(string my_string, int n) {
    string answer = "";
    reverse(my_string.begin(), my_string.end());
    answer = my_string.substr(0, n);
    reverse(answer.begin(), answer.end());
    return answer;
}