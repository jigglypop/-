import java.io.*;
import java.util.*;

public class Main {
    static String vowels = "aeiou";
    static int L;
    static int C;
    static char[] words;

    public static void comb(int k, int start, Stack<Character> chosen) {
        if (k == L) {
            StringBuffer sb = new StringBuffer();
            int vowel = 0;
            int consonant = 0;
            for (char c : chosen) {
                if (vowels.indexOf(c) == -1) {
                    consonant++;
                } else {
                    vowel++;
                }
                sb.append(c);
            }
            if (vowel >= 1 && consonant >= 2) {
                System.out.println(sb);
            }
            return;
        }
        for (int i = start; i < C; i++) {
            chosen.push(words[i]);
            comb(k + 1, i + 1, chosen);
            chosen.pop();
        }

    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        words = new char[C];
        for (int i = 0; i < C; i++) {
            char c = st.nextToken().charAt(0);
            words[i] = c;
        }
        Arrays.sort(words);
        Stack<Character> chosen = new Stack<Character>();
        comb(0, 0, chosen);
    }
}
