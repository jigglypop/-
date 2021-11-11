import java.io.*;
import java.util.*;

public class MainC {

    static class Pair {
        int y, x;

        public Pair(int y, int x) {
            this.y = y;
            this.x = x;
        }

    }
    
    static StringTokenizer st;
    static char[][] board = new char[5][10];
    static boolean[] hexa = new boolean[12];
    

    public static void main(String[] args) throws Exception{
        System.setIn(new FileInputStream("./3967.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Pair> point = new ArrayList<>();
        for (int y = 0; y < 5; y++) {
            String b = br.readLine();
            for (int x = 0; x < 9; x++) {
                char temp = b.charAt(x);
                String p = "x.";
                if (temp == p.charAt(0)) {
                    point.add(new Pair(y, x));
                }
                if (temp != p.charAt(0) && temp != p.charAt(1)) {
                    hexa[(int) temp - 65] = true;
                }
                board[y][x] = temp;
            }
        }
        for (int y = 0; y < 5; y++) {
            for (int x = 0; x < 9; x++) {
                System.out.print(board[y][x]);
            }    
            System.out.println();
        }
    }
}
