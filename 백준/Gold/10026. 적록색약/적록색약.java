import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int N;
    static char[][] grid;
    static int per1Num, per2Num;
    static boolean[][] visited;
    static int[] dxs = {-1, 0, 1, 0};
    static int[] dys = {0, 1, 0, -1};

    static boolean inRange(int x, int y) { // 범위 체크
        return 0 <= x && x < N && 0 <= y && y < N;
    }

    static void dfs(int x, int y, char color, int flag) {
        visited[x][y] = true;

        for (int i = 0; i < 4; i++) {
            int nx = x + dxs[i];
            int ny = y + dys[i];

            if (inRange(nx, ny) && !visited[nx][ny]) {
                char nextColor = grid[nx][ny];

                if (flag == 0 && color == nextColor) {
                    dfs(nx, ny, nextColor, flag);
                } else if (flag == 1) { // 적록색약인 경우
                    if (color == nextColor || (color == 'R' && nextColor == 'G') || (color == 'G' && nextColor == 'R')) {
                        dfs(nx, ny, nextColor, flag);
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        grid = new char[N][N];

        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            for (int j = 0; j < N; j++) {
                grid[i][j] = s.charAt(j);
            }
        }

        // 적록색약이 없는 사람이 볼 때
        visited = new boolean[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (!visited[i][j]) {
                    per1Num++;
                    dfs(i, j, grid[i][j], 0);
                }
            }
        }

        // 적록색약이 있는 사람이 볼 때
        visited = new boolean[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (!visited[i][j]) {
                    per2Num++;
                    dfs(i, j, grid[i][j], 1);
                }
            }
        }

        System.out.println(per1Num + " " + per2Num);
    }
}