#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

long long solution(long long n) {
    long long answer = 0;
    string str = to_string(n);
    for(int i = 0; i<str.size(); i ++){
        sort(str.rbegin(), str.rend());
    }

    return stoll(str);
}