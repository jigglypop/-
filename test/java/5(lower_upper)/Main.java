
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

// }

// 3. lower_bound, upper_bound

// public static int lower_bound(int[] nums, int M) {
//     int start = 0;
//     int end = nums.length;
//     int result = 0;
//     while (start <= end) {
//         int mid = (int) (start + end) / 2;
//         int temp = nums[mid];
//         if (temp >= M) {
//             result = mid;
//             end = mid - 1;
//         } else {
//             start = mid + 1;
//         }
//     }
//     return result;
// }

// public static int upper_bound(int[] nums, int M) {
//     int start = 0;
//     int end = nums.length;
//     while (start <= end) {
//         int mid = (int) (start + end) / 2;
//         int temp = nums[mid];
//         if (temp <= M) {
//             start = mid + 1;
//         } else {
//             end = mid - 1;
//         }
//     }
//     return start;
// }

import java.util.*;
import java.io.*;

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