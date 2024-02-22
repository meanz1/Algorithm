import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static int N, M, D, result, tempResult, enemyCnt;
	static char[][] grid;
	static int[] selected;
	static boolean[] isSelected;
	static int idx;
	public static class Pos{
		int x, y;
		public Pos(int x, int y){
			this.x = x;
			this.y = y;
		}
	}
	public static class Enemy{
		int x, y, dis;
		public Enemy(int x, int y, int dis) {
			this.x = x; // r
			this.y = y; // c
			this.dis = dis; // 거리
 		}
	}
	public static void selectEnemy() { // 세 개의 Enemy 선택해줄거임.
		Enemy[] es; // selected랑 동일시됨
		List<Pos> list = new ArrayList<>();
		tempResult = 0;
		int tempEnemyCnt = enemyCnt; // 적 개수 : tempEnemyCnt가 0이 되면 더이상 돌 필요 없음
		int startIdx = N; // N번은 돌아야함(while 기본)
		int start = N-D+1;
		int end = start+D;

		while(startIdx-->0) { // N번만큼 돌아야함
			es = new Enemy[3];
			if(start < 1) start = 1;
			for (int cur = 0; cur < 3; cur++) { // 각각의 적들
				for (int i = start; i < end; i++) {
					for (int j = 0; j < M; j++) {
						if (grid[i][j] == '1') {
							int distance = Math.abs(idx - i) + Math.abs(selected[cur] - j); // 거리
							if (distance > D)
								continue; // D보다 크면 넘어감
							// 현재 거리가 D보다 작거나 같을 때
							if (es[cur] == null) { // 만약에 비어있으면
								es[cur] = new Enemy(i, j, distance);
							} else if (es[cur].dis > distance) { // 기존의 거리가 크거나 같으면
								es[cur] = new Enemy(i, j, distance);
							} else if (es[cur].dis == distance) { // 기존의 거리와 같으면
								// 열 기준으로 왼쪽에 있는지 확인하여 갱신
								if (es[cur].y > j) {
									es[cur] = new Enemy(i, j, distance);
								}
							}
						}
					}
				}
			}

			boolean[][] checked = new boolean[N+1][M];
			for(int i=0; i<3; i++) {
				if(es[i]==null) continue;
				checked[es[i].x][es[i].y] = true;
			}
			for(int i=1; i<=N; i++){
				for(int j=0; j<M; j++) {
					if (checked[i][j]) {
						tempResult++;
						grid[i][j] = '0';
						list.add(new Pos(i, j));
						tempEnemyCnt--;
					}
				}
			}
			if(tempEnemyCnt == 0) {
				break;
			}
			idx --;
			start --;
			end--;

		}
		for(Pos p: list){
			grid[p.x][p.y] = '1';
		}
		result = Math.max(tempResult, result);
	}
	
	public static void combination(int start, int count) {
		if(count == 3) {
			idx= N+1;
			selectEnemy();
			return;
		}
		
		for(int i=start; i<M; i++) {
			if(isSelected[i]) continue;
			selected[count] = i;
			isSelected[i] = true;
			combination(i+1, count+1);
			isSelected[i] = false;
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		D = Integer.parseInt(st.nextToken());
		
		// 0행은 다 '0'으로 채워줌
		grid = new char[N+1][M];
		for(int i=0; i<M; i++) {
			grid[0][i] = '0';
		}
		
		// grid 값 넣어줌
		for(int i=1; i<=N; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<M; j++) {
				grid[i][j] = st.nextToken().charAt(0);
				if(grid[i][j] == '1') enemyCnt++; // 총 갯수 늘려줌
			}
		}
		selected = new int[3];
		isSelected = new boolean[M];
		
		combination(0, 0);
		
		System.out.println(result);
	}

}