
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

// 3. Node

// class Node {
//     int left, right;

//     Node(int left, int right) {
//         this.left = left;
//         this.right = right;
//     }
// }

// 4. travel

// static void preorder(Node[] words, int x) {
//     if (x == -1)
//         return;
//     System.out.print((char) (x + 'A'));
//     preorder(words, words[x].left);
//     preorder(words, words[x].right);
// }

// static void inorder(Node[] words, int x) {
//     if (x == -1)
//         return;
//     inorder(words, words[x].left);
//     System.out.print((char) (x + 'A'));
//     inorder(words, words[x].right);
// }

// static void postorder(Node[] words, int x) {
//     if (x == -1)
//         return;
//     postorder(words, words[x].left);
//     postorder(words, words[x].right);
//     System.out.print((char) (x + 'A'));
// }

class TreeMain {

    private static void solution(int sizeOfMatrix, int[][] matrix) {
        // TODO: 이곳에 코드를 작성하세요.
        // System.out.println(sizeOfMatrix);
        System.out.println("TreeMain");

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