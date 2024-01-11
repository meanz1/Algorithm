import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int[] stairs = new int[num];
        int[] dp = new int[num];
        for(int i = 0; i < num; i++){
            stairs[i] = sc.nextInt();
            dp[i] = 0;
        }
        if(num<=2){
            int sum = 0;
            for(int i: stairs)
                sum += i;
            System.out.println(sum);
        }
        else{
            dp[0] = stairs[0];
            dp[1] = stairs[0] + stairs[1];
            for (int i = 2; i < num; i++){
                if(i==2){
                    dp[i] = Math.max(stairs[1]+stairs[2], stairs[0]+stairs[2]);
                }
                else{
                    dp[i] = Math.max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i]);
                }
            }
            System.out.println(dp[num-1]);
        }
    }
}
