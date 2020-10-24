import java.io.FileInputStream;
import java.util.*;

public class Main {
    static int n;

    static LinkedList<Integer> choice;
    static LinkedList<Integer> nums;

    public static void comb(int k, int start, int m) {
        if (k == m) {
            StringBuilder sb = new StringBuilder();
            for (int i : choice)
                sb.append(i + " ");
            sb.append("\n");
            System.out.print(sb);
            return;
        }
        for (int i = start; i < n; i++) {
            choice.add(nums.get(i));
            comb(k + 1, i + 1, m);
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
        comb(0, 0, m);
    }
}
