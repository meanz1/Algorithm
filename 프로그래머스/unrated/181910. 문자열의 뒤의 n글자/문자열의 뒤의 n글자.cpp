#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string solution(string my_string, int n) {
    string answer = "";

    answer = my_string.substr(my_string.length()-n);

    return answer;
}