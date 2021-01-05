import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static LinkedList<Integer> choice;
    static LinkedList<Integer> nums;

    public static void perm(int k, int m, int used) {
        if (k == m) {
            StringBuilder sb = new StringBuilder();
            for (int i : choice)
                sb.append(i + " ");
            sb.append("\n");
            System.out.print(sb);
            return;
        }
        for (int i = 0; i < n; i++) {
            if ((used & (1 << i)) != 0)
                continue;
            choice.add(nums.get(i));
            perm(k + 1, m, used | (1 << i));
            choice.removeLast();
        }
    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        int m = sc.nextInt();
        nums = new LinkedList<>();
        choice = new LinkedList<>();
        for (int i = 0; i < n; i++)
            nums.add(sc.nextInt());
        nums.sort(null);
        perm(0, m, 0);
    }
}
