import java.io.FileInputStream;
import java.util.*;

public class Permutation {
    static boolean[] chosen = new boolean[10];
    static int[] nums = new int[10];

    static void perm(int k, int start, int n, int m) {
        if (k == m) {
            for (int i = 0; i < m; i++) {
                System.out.print(nums[i]);
                if (i != m - 1) {
                    System.out.print(' ');
                }
            }
            System.out.println();
            return;
        }
        for (int i = start; i <= n; i++) {
            if (chosen[i])
                continue;
            chosen[i] = true;
            nums[k] = i;
            perm(k + 1, i + 1, n, m);
            chosen[i] = false;
        }
    }

    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("./permutation.txt"));
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        perm(0, 1, N, M);
    }
}
