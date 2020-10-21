import java.io.FileInputStream;
import java.util.*;

public class Main {
    static int n;
    static int m;
    static LinkedList<Integer> choice;
    static StringBuilder sb;
    static LinkedList<Integer> nums;

    public static void perm(int k, int used) {
        if (k == m) {
            for (int i : choice)
                sb.append(i + " ");
            sb.append("\n");
            return;
        }
        for (int i = 0; i < n; i++) {
            if ((used & (1 << i)) != 0)
                continue;
            choice.add(nums.get(i));
            perm(k + 1, used | (1 << i));
            choice.removeLast();
        }
    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        sb = new StringBuilder();
        nums = new LinkedList<>();
        choice = new LinkedList<>();
        for (int i = 0; i < n; i++)
            nums.add(sc.nextInt());
        nums.sort(null);

        perm(0, 0);
        System.out.println(sb.toString());
    }
}
