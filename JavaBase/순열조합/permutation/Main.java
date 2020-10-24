import java.io.FileInputStream;
import java.util.*;

public class Main {
    static int n;
    static int m;
    static LinkedList<Integer> choice;
    static LinkedList<Integer> nums;
    static boolean[] used;

    public static void perm(int k, int m) {
        if (k == m) {
            StringBuilder sb = new StringBuilder();
            for (int i : choice)
                sb.append(i + " ");
            sb.append("\n");
            System.out.print(sb);
            return;
        }
        for (int i = 0; i < n; i++) {
            if (used[i])
                continue;
            used[i] = true;
            choice.add(nums.get(i));
            perm(k + 1, m);
            used[i] = false;
            choice.removeLast();
        }
    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        nums = new LinkedList<>();
        choice = new LinkedList<>();
        used = new boolean[n];
        for (int i = 0; i < n; i++)
            nums.add(sc.nextInt());
        nums.sort(null);
        perm(0, m);
        // System.out.println(sb.toString());
    }
}
