import java.io.*;

class Pair {
    int y;
    int x;
    public Pair(int y, int x) {
        this.y = y;
        this.x = x;
    }
}

public class BucketBrigade {

    static int[][] visited = new int[10][10];

    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("./17198.txt"));
        int N = 10;
        char[][] board = new char[N][N];
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int y = 0; y < 10; y++) {
            String str = br.readLine();
            for (int x = 0; x < 10; x++) {
                board[y][x] = str.charAt(x);
            }
        }

        for (int y = 0; y < 10; y++) {
            for (int x = 0; x < 10; x++) {
                System.out.print(visited[y][x]);
            }
            System.out.println();
        }
    }
}
