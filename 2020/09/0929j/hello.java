import java.io.FileInputStream;
import java.util.Scanner;

public class hello {
    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int test_case = 1; test_case <= T; test_case++) {
            System.out.println("test");
        }
    }
}
