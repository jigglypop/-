
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
//
// 3. next_permutation
// public static int[] next_permutation(int[] nums) {
//     int N = nums.length;
//     int i = N - 1;
//     while (i > 0 && nums[i - 1] >= nums[i]) {
//         i -= 1;
//     }
//
//     if (i <= 0) {
//         return nums;
//     }
//
//     int j = N - 1;
//     while (nums[j] <= nums[i - 1]) {
//         j -= 1;
//     }
//
//     int temp = nums[i - 1];
//     nums[i - 1] = nums[j];
//     nums[j] = temp;
//
//     j = N - 1;
//     while (i < j) {
//         temp = nums[i];
//         nums[i] = nums[j];
//         nums[j] = temp;
//         i += 1;
//         j -= 1;
//     }
//     return nums;
// }

// 4. permutation
// static LinkedList<Integer> choice;
// static LinkedList<Integer> nums;
// static boolean[] used;

// public static void perm(int k, int m) {
//     if (k == m) {
//         StringBuilder sb = new StringBuilder();
//         for (int i : choice)
//             sb.append(i + " ");
//         sb.append("\n");
//         System.out.print(sb);
//         return;
//     }
//     for (int i = 0; i < n; i++) {
//         if (used[i])
//             continue;
//         used[i] = true;
//         choice.add(nums.get(i));
//         perm(k + 1, m);
//         used[i] = false;
//         choice.removeLast();
//     }
// }

// 5. permutation bit
// static LinkedList<Integer> choice;
// static LinkedList<Integer> nums;

// public static void perm(int k, int m, int used) {
//     if (k == m) {
//         StringBuilder sb = new StringBuilder();
//         for (int i : choice)
//             sb.append(i + " ");
//         sb.append("\n");
//         System.out.print(sb);
//         return;
//     }
//     for (int i = 0; i < n; i++) {
//         if ((used & (1 << i)) != 0)
//             continue;
//         choice.add(nums.get(i));
//         perm(k + 1, m, used | (1 << i));
//         choice.removeLast();
//     }
// }
// 6. combination

// static LinkedList<Integer> choice;
// static LinkedList<Integer> nums;

// public static void comb(int k, int start, int m) {
//     if (k == m) {
//         StringBuilder sb = new StringBuilder();
//         for (int i : choice)
//             sb.append(i + " ");
//         sb.append("\n");
//         System.out.print(sb);
//         return;
//     }
//     for (int i = start; i < n; i++) {
//         choice.add(nums.get(i));
//         comb(k + 1, i + 1, m);
//         choice.removeLast();
//     }
// }

// 7. subset

// for (int i = 0; i < N; i++) {
//     nums[i] = Integer.parseInt(st.nextToken());
// }

// for (int i = 1; i < (1 << N); i++) {
//     int sum = 0;
//     for (int k = 0; k < N; k++) {
//         if ((i & (1 << k)) != 0) {
//             sum += nums[k];
//         }
//     }
//     if (sum == S) {
//         count += 1;
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