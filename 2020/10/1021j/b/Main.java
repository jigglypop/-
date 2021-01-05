import java.io.FileInputStream;
import java.util.*;

public class Main {
    static boolean[] check = new boolean[10];
    static int[] nums = new int[10];

    static void perm(int k, int start, int N, int M) {
        if (k == M) {
            for (int i = 0; i < M; i++) {
                System.out.print(nums[i]);
                if (i != M - 1)
                    System.out.print(' ');
            }
            System.out.println();
            return;
        }
        for (int i = start; i <= N; i++) {
            if (check[i])
                continue;
            check[i] = true;
            nums[k] = i;
            perm(k + 1, i + 1, N, M);
            check[i] = false;
        }
    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        perm(0, 1, N, M);
    }
}
