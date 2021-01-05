import java.io.*;

public class Main {
    public static int divide(int x, int e) {
        if (x % e == 0) {
            return e;
        } else {
            return x % e;
        }
    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        int[] divnum = { 15, 28, 19 };
        for (int i = 1; i <= 15 * 28 * 19 + 1; i++) {
            int temp = 0;
            for (int j = 0; j < 3; j++) {
                if (divide(i, divnum[j]) != Integer.parseInt(line[j])) {
                    break;
                }
                temp += 1;
            }
            if (temp == 3) {
                System.out.println(i);
                break;
            }
        }
    }
}
