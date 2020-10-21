import java.io.FileInputStream;
import java.util.*;

public class Combination {
    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("./permutation.txt"));
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        System.out.println(N + M);

    }
}
