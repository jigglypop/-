import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String words = br.readLine() + " ";
        Queue<Character> S = new LinkedList<Character>();
        Stack<Character> temp = new Stack<Character>();
        int i = 0;
        while (i < words.length()) {
            char word = words.charAt(i);
            if (word == '<') {
                if (temp.size() != 0) {
                    while (!temp.isEmpty()) {
                        S.add(temp.pop());
                    }
                    i++;
                    S.add('<');
                }
                while (words.charAt(i) != '>') {
                    S.add(words.charAt(i));
                    i++;
                }
                S.add(words.charAt(i));
                i++;
            } else if (word == ' ') {
                while (!temp.isEmpty()) {
                    S.add(temp.pop());
                }
                i++;
                S.add(' ');
            } else {
                temp.add(word);
                i++;
            }
        }
        StringBuilder sb = new StringBuilder();
        while (!S.isEmpty()) {
            sb.append(S.remove());
        }
        System.out.println(sb);
    }
}
