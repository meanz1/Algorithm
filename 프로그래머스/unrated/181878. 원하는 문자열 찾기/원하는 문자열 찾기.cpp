#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(string myString, string pat) {
    int answer = 0;
    transform(myString.begin(), myString.end(), myString.begin(), ::tolower);
    transform(pat.begin(), pat.end(), pat.begin(), ::tolower);
    int pat_length = pat.length();
    if (myString.length() < pat.length())
        return answer;
    
    for (int i = 0; i < myString.length()-pat_length+1; i++){
        if(myString.substr(i, pat_length) == pat)
            return 1;
            
    }
    
    return answer;
}