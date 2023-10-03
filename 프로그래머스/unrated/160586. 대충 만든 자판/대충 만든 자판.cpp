#include <string>
#include <vector>
#include <map>

using namespace std;

vector<int> solution(vector<string> keymap, vector<string> targets) {
    vector<int> answer;
    map<char, int> m;
    map<char, int>::iterator iter;
    int n;
    
    for(int i = 0; i < keymap.size(); i ++){
        for(int j = 0; j < keymap[i].size(); j++){
            if(m.find(keymap[i][j])!=m.end() ){
                m[keymap[i][j]] = min(j+1, m[keymap[i][j]]);
            }
            else
                m[keymap[i][j]] = j+1;
        }
    }
    for (int i = 0; i < targets.size(); i++){
        int cnt = 0;
        for(int j = 0; j < targets[i].size(); j++){
            if (m.find(targets[i][j]) != m.end()){
                cnt += m[targets[i][j]];
            }
            else{
                cnt = -1;
                break;
            }
        }
        answer.push_back(cnt);
        
    }

    
    return answer;
}