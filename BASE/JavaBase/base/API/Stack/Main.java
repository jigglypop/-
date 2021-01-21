import java.util.*;

public class Main {
    public static void main(String args[]) throws Exception {
        Stack<String> S = new Stack<String>();
        S.push("a");
        S.push("b");
        S.push("c");
        for (String i : S) {
            System.out.print(i + " ");
        }
        System.out.println();
        S.pop();
        for (String i : S) {
            System.out.print(i + " ");
        }
    }
}
