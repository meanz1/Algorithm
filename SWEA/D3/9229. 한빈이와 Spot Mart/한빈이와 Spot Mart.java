import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
class Solution
{
	static int N, M;
    static int[] snacks, selected;
    static int weight;

    static void combination(int start, int cnt){
        if(cnt==2){
            int tempWeight = Arrays.stream(selected).sum();
            if(tempWeight <= M){
                weight = Math.max(weight, tempWeight);
            }
            return;
        }
        for(int i=start; i<N; i++){
            selected[cnt] = snacks[i];
            combination(i+1, cnt+1);
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());
        for(int t = 1; t<= T; t++){
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            weight = -1;
            snacks = new int[N];
            selected = new int[2];
            st = new StringTokenizer(br.readLine());
            for(int i=0; i<N; i++){
                snacks[i] = Integer.parseInt(st.nextToken());
            }
            combination(0, 0);
            System.out.println(String.format("#%d %d", t, weight));
        }
    }
}