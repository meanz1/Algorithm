import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    static int[] grid, visited;
    static Deque<Integer> q = new ArrayDeque<>();
    static int bfs(){
        q.offer(1); // 1부터 시작, visited 부분은 어차피 0임

        while(!q.isEmpty()){
            int now = q.poll();
            for(int i=1; i<=6; i++){
                int nx = now+i;

                if(nx>100) continue; // nx가 100 초과면 continue

                if(visited[grid[nx]] == 0){ // 방문 안했으면
                    visited[grid[nx]] = visited[grid[now]]+1; // 이전 값 +1
                    q.offer(grid[nx]);
                }
//                else { // 방문 했으면, 작은 값 넣어주면 됨.. 근데 어차피 늦게 도착하는거는 무조건 오래걸리니까 이거 안써도 됨
//                    visited[grid[nx]] = Math.min(visited[grid[nx]], visited[grid[now]]+1);
//                }

                if(grid[nx]==100){
                    return visited[100];
                }
            }
        }

        return 0;
    }

    public static void main(String[] args) throws IOException {
        grid = new int[101];
        visited = new int[101];
        for(int i=1; i<=100; i++){
            grid[i] = i;
        }

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        for(int i=0; i<n+m; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            grid[a] = b;
        }

        int result = bfs();
        System.out.println(result);
    }
}