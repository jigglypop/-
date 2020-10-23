import java.io.*;

public class Main {
    static int n;
    static int count;

    public static void go(int sum) {
        if (sum == n) {
            count += 1;
            return;
        }
        if (sum > n) {
            return;
        }
        go(sum + 1);
        go(sum + 2);
        go(sum + 3);
    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            count = 0;
            n = Integer.parseInt(br.readLine());
            go(0);
            System.out.println(count);
        }
    }
}
