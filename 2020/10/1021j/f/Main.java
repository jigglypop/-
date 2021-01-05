import java.util.*;
import java.io.*;

public class Main {

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader bi = new BufferedReader(new InputStreamReader(System.in));
        String str = bi.readLine();
        int N = Integer.parseInt(bi.readLine());
        Stack<Character> front = new Stack<>();
        Stack<Character> back = new Stack<>();
        for (char ch : str.toCharArray()) {
            front.push(ch);
        }
        for (int i = 0; i < N; i++) {
            String[] line = bi.readLine().split(" ");
            char order = line[0].charAt(0);
            if (order == 'L') {
                if (!front.empty()) {
                    back.push(front.pop());
                }
            } else if (order == 'D') {
                if (!back.empty()) {
                    front.push(back.pop());
                }
            } else if (order == 'P') {
                char x = line[1].charAt(0);
                front.push(x);
            } else if (order == 'B') {
                if (!front.empty()) {
                    front.pop();
                }
            }
        }
        while (!front.empty()) {
            back.push(front.pop());
        }
        StringBuilder sb = new StringBuilder();
        while (!back.empty()) {
            sb.append(back.pop());
        }
        System.out.println(sb);
    }
}
