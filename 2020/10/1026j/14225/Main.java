import java.io.*;
import java.util.*;

public class Main {

    public static int[] DP;
    public static int[] nums;
    public static int Sum;
    public static int N;

    public static void go(int k, int Sum) {
        if (k == N) {
            DP[Sum] = 1;
            return;
        }
        go(k + 1, Sum + nums[k]);
        go(k + 1, Sum);
    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        nums = new int[N];
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        Sum = 0;
        for (int num : nums) {
            Sum += num;
        }
        DP = new int[Sum + 2];
        go(0, 0);

        for (int i = 1; i < Sum + 2; i++) {
            if (DP[i] == 0) {
                System.out.println(i);
                break;
            }
        }
    }
}
