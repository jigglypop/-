
// import java.util.*;
// import java.io.*;
// System.setIn(new FileInputStream("./input.txt"));

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

// 3. diagonal
//
// public static void diagonal(int[][] arr) {
//     int Y = arr.length;
//     int X = arr[0].length;

//     for (int diag = 0; diag < Y + X - 1; diag++) {
//         int y = diag < X ? 0 : diag - X + 1;
//         int x = diag < X ? diag : X - 1;
//         while (y < Y && x >= 0) {
//             System.out.printf("%d ", arr[y][x]);
//             y += 1;
//             x -= 1;
//         }
//         System.out.println();
//     }
// }

// 4. reverse

// public static void reverse(int[][] arr) {
//     int Y = arr.length;
//     int X = arr[0].length;
//     for (int x = 0; x < X; x++) {
//         for (int y = 0; y < Y; y++) {
//             System.out.printf("%d ", arr[y][x]);
//         }
//         System.out.println();
//     }
// }

// 5. zigzag

// public static void zigzag(int[][] arr) {
//     int Y = arr.length;
//     int X = arr[0].length;
//     for (int y = 0; y < Y; y++) {
//         if (y % 2 == 0) {
//             for (int x = 0; x < X; x++) {
//                 System.out.printf("%d ", arr[y][x]);
//             }
//         } else {
//             for (int x = X - 1; x >= 0; x--) {
//                 System.out.printf("%d ", arr[y][x]);
//             }
//         }
//         System.out.println();
//     }
// }

//  -1,-1   -1, 0    -1,1
//   0,-1    0, 0     0,1
//   1,-1    1, 0     1,1

import java.util.*;
import java.io.*;

class Main {

    public static void diagonal(int[][] arr) {
        int Y = arr.length;
        int X = arr[0].length;

        for (int diag = 0; diag < Y + X - 1; diag++) {
            int y = diag < X ? 0 : diag - X + 1;
            int x = diag < X ? diag : X - 1;
            while (y < Y && x >= 0) {
                System.out.printf("%d ", arr[y][x]);
                y += 1;
                x -= 1;
            }
            System.out.println();
        }
    }

    public static void reverse(int[][] arr) {
        int Y = arr.length;
        int X = arr[0].length;
        for (int x = 0; x < X; x++) {
            for (int y = 0; y < Y; y++) {
                System.out.printf("%d ", arr[y][x]);
            }
            System.out.println();
        }
    }

    public static void zigzag(int[][] arr) {
        int Y = arr.length;
        int X = arr[0].length;
        for (int y = 0; y < Y; y++) {
            if (y % 2 == 0) {
                for (int x = 0; x < X; x++) {
                    System.out.printf("%d ", arr[y][x]);
                }
            } else {
                for (int x = X - 1; x >= 0; x--) {
                    System.out.printf("%d ", arr[y][x]);
                }
            }
            System.out.println();
        }
    }

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