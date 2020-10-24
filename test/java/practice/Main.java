
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
// public static int dfs(int sy, int sx, int N, int[][] matrix) {
//     int dy[] = { -1, 1, 0, 0 };
//     int dx[] = { 0, 0, -1, 1 };

//     Stack<Pair> S = new Stack<Pair>();
//     boolean[][] visited = new boolean[N][N];
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
//             if (0 <= ny && ny < N && 0 <= nx && nx < N) {
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

class Main {

    private static void solution(int sizeOfMatrix, int[][] matrix) {
        // TODO: 이곳에 코드를 작성하세요.
        // System.out.println(sizeOfMatrix);
        int[] dist = new int[10];

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