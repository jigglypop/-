
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
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.*;

class MainC {

    public static ArrayList<String> Regex(String p, String text) {
        Pattern pattern = Pattern.compile(p);
        Matcher matcher = pattern.matcher(text);
        ArrayList<String> result = new ArrayList<>();
        while (matcher.find()) {
            result.add(matcher.group(0));
        }
        return result;
    }

    private static void solution(int numOfOrder, String[] orderArr) {
        // TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
        for (String order : orderArr) {
            // Stack<String> words = new Stack<>();
            System.out.print(Regex("/()/", order));
            String[] words = order.split("\\(");
            for (String word : words) {
                System.out.println(word);

            }
            int[] nums = new int[numOfOrder];

            // System.out.println(words);
            // for (int i = 0; i < order.length(); i++) {
            // char temp = order.charAt(i);
            // if (temp == '(' || temp == ')') {
            // if (!bracket.isEmpty()) {
            // bracket.push(temp);
            // } else {
            // if (temp == '(') {
            // bracket.push(temp);
            // } else {
            // if (bracket.peek() == '(') {
            // bracket.pop();
            // System.out.println("hello");
            // word = "";
            // } else {
            // bracket.push(temp);
            // }
            // }
            // }
            // } else {
            // word += temp;
            // }
            // }
            // System.out.println(bracket);
            // System.out.println(order);
        }
    }

    private static class InputData {
        int numOfOrder;
        String[] orderArr;
    }

    private static InputData processStdin() {
        InputData inputData = new InputData();

        try (Scanner scanner = new Scanner(System.in)) {
            inputData.numOfOrder = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));

            inputData.orderArr = new String[inputData.numOfOrder];
            for (int i = 0; i < inputData.numOfOrder; i++) {
                inputData.orderArr[i] = scanner.nextLine().replaceAll("\\s+", "");
            }
        } catch (Exception e) {
            throw e;
        }

        return inputData;
    }

    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("./inputC.txt"));

        InputData inputData = processStdin();

        solution(inputData.numOfOrder, inputData.orderArr);
    }
}