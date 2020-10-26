import java.io.*;
import java.util.*;

public class Main {

    static int N, K;
    static int[] words;
    static int Max;

    public static int makeBits(String s) {
        int result = 0;

        for (int i = 0; i < s.length(); i++) {
            result |= 1 << (s.charAt(i) - 'a');
        }

        return result;
    }

    public static void comb(int k, int start, int masked) {
        if (k == K - 5) {
            int count = 0;
            for (int word : words) {
                if ((word | masked) == masked) {
                    count++;
                }
            }
            Max = Math.max(count, Max);
        } else {
            for (int i = start; i < 26; i++) {
                if ((masked & (1 << i)) == 0) {
                    comb(k + 1, i, masked | (1 << i));
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        if (K < 5) {
            System.out.println(0);
            return;
        }
        int masked = makeBits("antic");
        words = new int[N];
        for (int n = 0; n < N; n++) {
            words[n] = makeBits(br.readLine());
        }
        Max = 0;
        comb(0, 0, masked);
        System.out.println(Max);
    }

}