import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int N, cnt;
    static int[] val;
    static int result;
    static int[][] link;
    static List<Integer>[] list;
    static boolean[] isSelected;
    static boolean[] visited;
    static List<Integer> listA, listB;

    static int dfs(List<Integer> tempList, boolean[] visited, int start){
        int cnt = 1;
        for(int i=0; i<tempList.size(); i++){
            if(link[start][tempList.get(i)] == 1 && !visited[i]){
                visited[i] = true;
                cnt += dfs(tempList, visited, tempList.get(i));
            }
        }
        return cnt;
    }
    static boolean isConnected(List<Integer> tempList){
        visited = new boolean[tempList.size()];
        visited[0] = true;
        int idx = 0;
        int start = tempList.get(idx);
        cnt = 1;
        return tempList.size() == dfs(tempList, visited, start);
    }
    static void subset(int cnt) {
        if (cnt == N + 1) {
            listA = new ArrayList<>();
            listB = new ArrayList<>();
            for (int i = 1; i <= N; i++) {
                if (isSelected[i]) {
                    listA.add(i);
                } else {
                    listB.add(i);
                }
            }

            if (listA.isEmpty() || listB.isEmpty()) return;
            // a, b가 연결되어있는지 확인해야함.

            if(!isConnected(listA) || !isConnected(listB)) return;


            int sumA = 0, sumB = 0;
            for (int i : listA) {
                sumA += val[i];
            }
            for (int i : listB) {
                sumB += val[i];
            }
            // 결과 갱신
            result = Math.min(result, Math.abs(sumA - sumB));

            // 차이가 0이면 그냥 종료
            if (result == 0) {
                System.out.println(0);
                System.exit(0);
            }
            return;
        }
        // 부분집합 생성
        isSelected[cnt] = true;
        subset(cnt + 1);
        isSelected[cnt] = false;
        subset(cnt + 1);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        val = new int[N + 1];
        st = new StringTokenizer(br.readLine());

        for (int i = 1; i <= N; i++) {
            val[i] = Integer.parseInt(st.nextToken());
        }

        link = new int[N+1][N+1];
        for(int i=1; i<=N; i++){
            st = new StringTokenizer(br.readLine());
            int temp = Integer.parseInt(st.nextToken());
            for (int t = 0; t < temp; t++) {
                int node = Integer.parseInt(st.nextToken());
                link[i][node] = 1;
                link[node][i] = 1; // 양방향 리스트 연결
            }
        }

        br.close();
        isSelected = new boolean[N + 1];
        result = Integer.MAX_VALUE;
        subset(1);
        result = (result == Integer.MAX_VALUE) ? -1 : result;
        System.out.println(result);
    }
}