import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int[] nums;
    static int[] selected;

    public static void combinations(int start, int count){
        if(count == 6){
            for(int i=0; i<6; i++) System.out.print(selected[i]+" ");
            System.out.println();
            return;
        }

        for(int i=start; i<n; i++){
            selected[count] = nums[i];
            combinations(i+1, count+1);
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true){
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            if(n==0) break;
            nums = new int[n];
            selected = new int[6];
            for(int i=0; i<n; i++){
                nums[i] = Integer.parseInt(st.nextToken());
            }
            combinations(0, 0);
            System.out.println();
        }
    }
}