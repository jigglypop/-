import java.io.*;
import java.util.*;

public class Main {
    static StringTokenizer st;

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());
        int count = 0;
        int[] nums = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1; i < (1 << N); i++) {
            int sum = 0;
            for (int k = 0; k < N; k++) {
                if ((i & (1 << k)) != 0) {
                    sum += nums[k];
                }
            }
            if (sum == S) {
                count += 1;
            }
        }
        System.out.println(count);
    }
}
