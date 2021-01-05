import java.io.FileInputStream;
import java.util.*;

public class Main {
    static int n;
    static int m;
    static LinkedList<Integer> result;
    static StringBuilder sb;
    static LinkedList<Integer> nums;

    public static void perm(int count) {
        if (count == m) {
            for (int i : result)
                sb.append(i + " ");
            sb.append("\n");
            return;
        }
        for (int i = 0; i < n; i++) {
            result.add(nums.get(i));
            perm(count + 1);
            result.removeLast();
        }
    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        sb = new StringBuilder();
        nums = new LinkedList<>();
        result = new LinkedList<>();
        for (int i = 0; i < n; i++)
            nums.add(sc.nextInt());
        nums.sort(null);
        perm(0);
        System.out.println(sb.toString());
    }
}
