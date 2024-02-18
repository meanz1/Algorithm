class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        for (String skillTree : skill_trees) {
            int idx = 0;
            int check = 0;

            for (int j = 0; j < skillTree.length(); j++) {
                if (skill.indexOf(skillTree.charAt(j)) != -1) {
                    check++;
                }
                if (skillTree.charAt(j) == skill.charAt(idx)) {
                    idx++;
                    if (idx == skill.length()) break;
                }
            }
            if (check == idx) answer++;
        }
        return answer;
    }
}