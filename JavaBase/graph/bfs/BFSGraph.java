import java.io.*;
import java.util.*;

public class BFSGraph {

    private static int N;
    private static int[][] map;
    private static StringBuilder sb = new StringBuilder();
    private static int[] dy = { -1, 1, 0, 0 };
    private static int[] dx = { 0, 0, -1, 1 };
    private static ArrayList<Integer> list = new ArrayList<>();

    private static class Pair {
        int y;
        int x;

        public Pair(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    public static void main(String[] args) throws NumberFormatException, IOException {
        System.setIn(new FileInputStream("./inputB.txt"));

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        map = new int[N][N];

        for (int y = 0; y < N; y++) {
            String str = br.readLine();
            for (int x = 0; x < N; x++) {
                map[y][x] = str.charAt(x) - '0';
            }
        }

        int count = 0;
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                if (map[y][x] == 1) {
                    bfs(y, x);
                    count++;
                }
            }
        }

        Collections.sort(list);

        sb.append(count).append('\n');
        for (int cnt : list) {
            sb.append(cnt).append('\n');
        }

        System.out.println(sb);
    }

    private static void bfs(int y, int x) {
        Queue<Pair> Q = new LinkedList<Pair>();
        Q.add(new Pair(y, x));
        int count = 1;
        map[y][x] = 0;

        while (!Q.isEmpty()) {
            Pair q = Q.remove();
            y = q.y;
            x = q.x;
            for (int i = 0; i < 4; i++) {
                int ny = y + dy[i];
                int nx = x + dx[i];

                if (0 <= ny && ny < N && 0 <= nx && nx < N) {
                    if (map[ny][nx] == 1) {
                        Q.add(new Pair(ny, nx));
                        map[ny][nx] = 0;
                        count++;
                    }
                }
            }
        }
        list.add(count);
    }

}
