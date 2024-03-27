import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static int n, m;
	static char[][] grid;
	static int exitNum; // 문의 개수
	static boolean[][][] visited;
	static Deque<Node> q = new ArrayDeque<>();
	static int[] dxs = {-1, 0, 1, 0};
	static int[] dys = {0, 1, 0, -1};
	static class Node{ // 내 현재 위치 넣어줘야하니까.
		int x;
		int y;
		int time; // 이동 시간
		int key; // 갖고 있는 키들
		Node(int x, int y, int t, int k){
			this.x = x;
			this.y = y;
			this.time = t;
			this.key = k;
		}
	}
	
	static boolean inRange(int x, int y) {		
		return 0<=x && x<n && 0<=y && y<m; // 범위안에 있는거
	}
	
	static int bfs() {
		int curX, curY, curK, curT;
		int nx, ny;
		while(!q.isEmpty()) {
			Node cur = q.poll();
			curX = cur.x;
			curY = cur.y;
			curK = cur.key;
			curT = cur.time;
			
			if(grid[curX][curY] == '1')
				return curT;
			for(int i=0; i<4; i++) {
				nx = dxs[i]+curX;
				ny = dys[i]+curY;

				if(!inRange(nx, ny) || grid[nx][ny] == '#' || visited[nx][ny][curK]){
					continue;
				}

				// 만약에 열쇠면
				if(grid[nx][ny] >= 'a' && grid[nx][ny] <='f'){
					int key = curK | (1<<(grid[nx][ny]-'a')); // 키 값 갱신
					q.add(new Node(nx, ny, curT+1, key));
					visited[nx][ny][key] = true;
				}

				// 만약에 문이면
				else if (grid[nx][ny] >= 'A' && grid[nx][ny] <= 'F'){
					boolean flag = (curK & (1 << (grid[nx][ny] - 'A'))) != 0; // 현재 내가 가지고 있는 키인지 확인
					if(flag) { // 키 가지고 있다면
						q.add(new Node(nx, ny, curT+1, curK));
						visited[nx][ny][curK] = true;
					}
				}

				// 그외 (.이나 도착지라면)
				else{
					q.add(new Node(nx, ny, curT+1, curK));
					visited[nx][ny][curK] = true;
				}
			}
		}
		
		return -1;
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		grid = new char[n][m];
		visited = new boolean[n][m][1<<6]; // 6개의 키를 써야하니까 2^6만큼의 공간 필요함
		for(int i=0; i<n; i++) {
			String s = br.readLine();
			for(int j=0; j<m; j++) {
				grid[i][j] = s.charAt(j);
				if(grid[i][j] == '0') {
					q.add(new Node(i, j, 0, 0)); // 시작점 넣어줌
					visited[i][j][0] = true;
					grid[i][j] = '.';
				} 
				
			}
		}

		System.out.println(bfs());
	}

}