import java.io.FileInputStream;
import java.util.Scanner;

public class a {

    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("./a.txt"));
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        System.out.printf("%d %d", N, M);
    }
}
