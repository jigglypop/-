
// import java.util.*;
// import java.io.*;
// System.setIn(new FileInputStream("./input.txt"));
import java.util.*;

import javax.swing.text.DefaultStyledDocument.ElementSpec;

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

import java.util.*;
import java.io.*;

class MainB {
    private static void solution(int day, int width, int[][] blocks) {
        int result = 0;
        int[] temp = new int[width];
        for (int i = 0; i < day; i++) {
            for (int j = 0; j < width; j++) {
                temp[j] += blocks[i][j];
            }
            int left = 0;
            int right = temp.length - 1;
            int left_max = temp[left];
            int right_max = temp[right];
            while (left < right) {
                left_max = Math.max(temp[left], left_max);
                right_max = Math.max(temp[right], right_max);
                if (left_max < right_max) {
                    result += left_max - temp[left];
                    temp[left] += left_max - temp[left];
                    left += 1;
                } else {
                    result += right_max - temp[right];
                    temp[right] += right_max - temp[right];
                    right -= 1;
                }
            }
        }
        System.out.println(result);
    }

    private static class InputData {
        int day;
        int width;
        int[][] blocks;
    }

    private static InputData processStdin() {
        InputData inputData = new InputData();

        try (Scanner scanner = new Scanner(System.in)) {
            inputData.day = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));
            inputData.width = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));

            inputData.blocks = new int[inputData.day][inputData.width];
            for (int i = 0; i < inputData.day; i++) {
                String[] buf = scanner.nextLine().trim().replaceAll("\\s+", " ").split(" ");
                for (int j = 0; j < inputData.width; j++) {
                    inputData.blocks[i][j] = Integer.parseInt(buf[j]);
                }
            }
        } catch (Exception e) {
            throw e;
        }

        return inputData;
    }

    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("./inputB.txt"));
        InputData inputData = processStdin();
        solution(inputData.day, inputData.width, inputData.blocks);
    }
}