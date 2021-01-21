
// import java.util.*;
// import java.io.*;
// System.setIn(new FileInputStream("./input.txt"));
import java.util.*;
import java.io.*;

// 1. print
//
// public static void Print(int[][] matrix) {
//     for (int[] nums : matrix) {
//         for (int num : nums) {
//             System.out.print(num + " ");
//         }
//         System.out.println();
//     }
// }
//
// 2. pair
//
// class Pair {
//     int y;
//     int x;

//     Pair(int y, int x) {
//         this.y = y;
//         this.x = x;
//     }
// }
//
// 3. dfs
// public static int dfs(int sy, int sx, int Y, int X, int[][] matrix) {
//     int dy[] = { -1, 1, 0, 0 };
//     int dx[] = { 0, 0, -1, 1 };

//     Stack<Pair> S = new Stack<Pair>();
//     boolean[][] visited = new boolean[Y][X];
//     S.push(new Pair(sy, sx));
//     visited[sy][sx] = true;
//     int count = 1;
//     while (!S.isEmpty()) {
//         Pair s = S.pop();
//         int y = s.y;
//         int x = s.x;
//         for (int i = 0; i < 4; i++) {
//             int ny = y + dy[i];
//             int nx = x + dx[i];
//             if (0 <= ny && ny < Y && 0 <= nx && nx < X) {
//                 if (!visited[ny][nx] && matrix[ny][nx] == 1) {
//                     visited[ny][nx] = true;
//                     matrix[ny][nx] = 0;
//                     count += 1;
//                     S.push(new Pair(ny, nx));
//                 }
//             }
//         }
//     }
//     return count;
// }
//

// 4. bfs
// public static void bfs(int sy, int sx, int Y, int X, int[][] matrix) {
//     int[] dy = { 1, -1, 0, 0 };
//     int[] dx = { 0, 0, 1, -1 };

//     int[][] visited = new int[Y][X];

//     Queue<Pair> Q = new LinkedList<Pair>();
//     Q.add(new Pair(sy, sx));
//     visited[sy][sx] = cnt;

//     while (!Q.isEmpty()) {
//         Pair p = Q.remove();
//         int y = p.y;
//         int x = p.x;
//         for (int i = 0; i < 8; i++) {
//             int ny = y + dy[i];
//             int nx = x + dx[i];
//             if (0 <= nx && nx < X && 0 <= ny && ny < Y) {
//                 if (matrix[ny][nx] == 1 && visited[ny][nx] == 0) {
//                     Q.add(new Pair(ny, nx));
//                     visited[ny][nx] = cnt;
//                 }
//             }
//         }
//     }
// }

// 4. dijkstra
// class Edge implements Comparable<Edge> {
//     int to, cost;

//     Edge(int to, int cost) {
//         this.to = to;
//         this.cost = cost;
//     }

//     @Override
//     public int compareTo(Edge that) {
//         return Integer.compare(this.cost, that.cost);
//     }
// }

// public static int[] dijkstra(List<Edge>[] graph, int start, int N) {
//     int[] dist = new int[N + 1];
//     Arrays.fill(dist, Integer.MAX_VALUE);

//     PriorityQueue<Edge> PQ = new PriorityQueue<>();
//     PQ.add(new Edge(start, 0));
//     dist[start] = 0;

//     while (!PQ.isEmpty()) {
//         Edge x = PQ.remove();
//         int u = x.to;
//         int w = x.cost;
//         if (dist[u] >= w) {
//             for (Edge y : graph[u]) {
//                 int v = y.to;
//                 int dw = y.cost;
//                 if (dist[v] > dist[u] + dw) {
//                     dist[v] = dist[u] + dw;
//                     PQ.add(new Edge(v, dist[v]));
//                 }
//             }
//         }
//     }
//     return dist;
// }

// 5. floyd

// int[][] graph = new int[n + 1][n + 1];
// for (int y = 1; y <= n; y++) {
//     for (int x = 1; x <= n; x++) {
//         if (y == x) {
//             graph[y][x] = 0;
//         } else {
//             graph[y][x] = INF;
//         }
//     }
// }
// for (int i = 0; i < m; i++) {
//     st = new StringTokenizer(br.readLine());
//     int a = Integer.parseInt(st.nextToken());
//     int b = Integer.parseInt(st.nextToken());
//     int c = Integer.parseInt(st.nextToken());
//     if (graph[a][b] > c) {
//         graph[a][b] = c;
//     }
// }

// public static int[][] floyd(int[][] graph, int N) {
//     for (int k = 1; k <= N; k++) {
//         for (int y = 1; y <= N; y++) {
//             for (int x = 1; x <= N; x++) {
//                 if (graph[y][x] > graph[y][k] + graph[k][x]) {
//                     graph[y][x] = graph[y][k] + graph[k][x];
//                 }
//             }
//         }
//     }
//     return graph;
// }

// 6. DAG

// List<Integer>[] graph = new List[N + 1];
// for (int i = 1; i <= N; i++) {
//     graph[i] = new ArrayList<Integer>();
// }
// int[] check = new int[N + 1];
// for (int i = 0; i < M; i++) {
//     st = new StringTokenizer(br.readLine());
//     int a = Integer.parseInt(st.nextToken());
//     int b = Integer.parseInt(st.nextToken());
//     graph[a].add(b);
//     check[b] += 1;
// }
// Queue<Integer> Q = new LinkedList<Integer>();
// for (int i = 1; i <= N; i++) {
//     if (check[i] == 0) {
//         Q.add(i);
//     }
// }
// while (!Q.isEmpty()) {
//     int u = Q.remove();
//     System.out.print(u + " ");
//     for (int v : graph[u]) {
//         check[v] -= 1;
//         if (check[v] == 0) {
//             Q.add(v);
//         }
//     }
// }

class Main {

    private static void solution(int sizeOfMatrix, int[][] matrix) {
        // TODO: 이곳에 코드를 작성하세요.
        // System.out.println(sizeOfMatrix);

    }

    private static class InputData {
        int sizeOfMatrix;
        static int[][] matrix;
    }

    private static InputData processStdin() {
        InputData inputData = new InputData();

        try (Scanner scanner = new Scanner(System.in)) {
            inputData.sizeOfMatrix = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));

            inputData.matrix = new int[inputData.sizeOfMatrix][inputData.sizeOfMatrix];
            for (int i = 0; i < inputData.sizeOfMatrix; i++) {
                String[] buf = scanner.nextLine().trim().replaceAll("\\s+", " ").split(" ");
                for (int j = 0; j < inputData.sizeOfMatrix; j++) {
                    inputData.matrix[i][j] = Integer.parseInt(buf[j]);
                }
            }
        } catch (Exception e) {
            throw e;
        }

        return inputData;
    }

    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        InputData inputData = processStdin();
        solution(inputData.sizeOfMatrix, inputData.matrix);
    }
}