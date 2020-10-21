import java.io.FileInputStream;
import java.util.*;

public class Main {
    static int n;
    static int m;
    static LinkedList<Integer> choice;
    static StringBuilder sb;
    static LinkedList<Integer> nums;

    public static void comb(int k, int start) {
        if (k == m) {
            for (int i : choice)
                sb.append(i + " ");
            sb.append("\n");
            return;
        }
        for (int i = start; i < n; i++) {
            choice.add(nums.get(i));
            comb(k + 1, i + 1);
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
        comb(0, 0);
        System.out.println(sb.toString());
    }
}
