import java.util.*;
import java.io.*;

public class Main {

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(bf.readLine());
        while (N-- > 0) {
            String str = bf.readLine() + "\n";
            Stack<Character> S = new Stack<>();
            for (char ch : str.toCharArray()) {
                if (ch == '\n' || ch == ' ') {
                    while (!S.isEmpty()) {
                        bw.write(S.pop());
                    }
                    bw.write(ch);
                } else {
                    S.push(ch);
                }
            }
        }
        bw.flush();
    }
}
