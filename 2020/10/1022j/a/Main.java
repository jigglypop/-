import java.io.*;
import java.util.*;

public class Main {
    static StringTokenizer st;

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int Y = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());
        int[][] board = new int[Y][X];
        for (int y = 0; y < Y; y++) {
            st = new StringTokenizer(br.readLine());
            String s = st.nextToken();
            for (int x = 0; x < X; x++) {
                board[y][x] = s.charAt(x) - '0';
            }
        }

    }
}
