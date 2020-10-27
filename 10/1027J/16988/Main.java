import java.io.*;
import java.util.*;

class Pair {
    int y;
    int x;

    Pair(int y, int x) {
        this.y = y;
        this.x = x;
    }
}

public class Main {
    public static int Y;
    public static int X;
    public static int[][] map;
    public static int[] dy = { -1, 1, 0, 0 };
    public static int[] dx = { 0, 0, -1, 1 };
    public static Stack<Pair> re;

    public static int dfs(int sy, int sx) {
        Stack<Pair> S = new Stack<>();
        boolean[][] visited = new boolean[Y][X];
        visited[sy][sx] = true;
        map[sy][sx] = 0;
        S.push(new Pair(sy, sx));
        int count = 1;
        int not = 0;
        while (!S.isEmpty()) {
            Pair s = S.pop();
            int y = s.y;
            int x = s.x;
            for (int i = 0; i < 4; i++) {
                int ny = y + dy[i];
                int nx = x + dx[i];
                if (0 <= ny && ny < Y && 0 <= nx && nx < X) {
                    if (map[ny][nx] == 0 && visited[ny][nx] == false) {
                        not += 1;
                    } else if (map[ny][nx] == 2 && visited[ny][nx] == false) {
                        map[ny][nx] = 0;
                        visited[ny][nx] = true;
                        count += 1;
                        S.push(new Pair(ny, nx));
                    }
                }
            }
        }
        return not == 0 ? count : 0;
    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        Y = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());
        map = new int[Y][X];
        re = new Stack<Pair>();

        for (int y = 0; y < Y; y++) {
            st = new StringTokenizer(br.readLine());
            for (int x = 0; x < X; x++) {
                int temp = Integer.parseInt(st.nextToken());
                if (temp == 2) {
                    re.push(new Pair(y, x));
                }
                map[y][x] = temp;
            }
        }
        int Max = 0;
        for (int y1 = 0; y1 < Y; y1++) {
            for (int x1 = 0; x1 < X; x1++) {
                for (int y2 = 0; y2 < Y; y2++) {
                    for (int x2 = 0; x2 < X; x2++) {
                        if (map[y1][x1] == 0 && map[y2][x2] == 0) {
                            map[y1][x1] = 1;
                            map[y2][x2] = 1;
                            int count = 0;
                            for (int y = 0; y < Y; y++) {
                                for (int x = 0; x < X; x++) {
                                    if (map[y][x] == 2) {
                                        count += dfs(y, x);
                                    }
                                }
                            }
                            Max = Math.max(Max, count);
                            map[y1][x1] = 0;
                            map[y2][x2] = 0;
                            for (Pair p : re) {
                                int ry = p.y;
                                int rx = p.x;
                                map[ry][rx] = 2;
                            }
                        }
                    }
                }
            }
        }
        System.out.println(Max);
    }
}
