import java.io.FileInputStream;
import java.util.Scanner;

public class a {

    public static void main(String[] args) throws Exception {
        int i = 0;
        int sum = 0;
        while (i < 10) {
            i++;
            if (i % 2 == 1) {
                continue;
            }
            sum += i;
        }
        System.out.print(sum);

    }
}
