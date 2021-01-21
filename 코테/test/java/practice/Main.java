
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

// 4. pair

// class Pair implements Comparable<Pair> {
//     int x;
//     int y;

//     public Pair(int x, int y) {
//         this.x = x;
//         this.y = y;
//     }

//     @Override
//     public int compareTo(Pair that) {
//         if (this.x == that.x) {
//             return this.y - that.y;
//         }
//         return this.x - that.x;
//     }
// }
// PriorityQueue<Pair> pq = new PriorityQueue<Pair>();
// int N = Integer.parseInt(br.readLine());
// StringBuilder sb = new StringBuilder();
// StringTokenizer st;
// for (int i = 0; i < N; i++) {
//     st = new StringTokenizer(br.readLine());
//     int x = Integer.parseInt(st.nextToken());
//     int y = Integer.parseInt(st.nextToken());
//     pq.add(new Pair(x, y));
// }
// while (!pq.isEmpty()) {
//     sb.append(pq.peek().x).append(" ").append(pq.poll().y).append("\n");
// }

import java.util.*;
import java.io.*;

class Main {

    public static void PrintChar(char[] matrix) {
        for (char nums : matrix) {
            System.out.print(nums + " ");
        }
    }

    public static void PrintInt(int[] matrix) {
        for (int nums : matrix) {
            System.out.print(nums + " ");
        }
    }

    public static void PrintLink(LinkedList<Character> matrix) {
        for (Character nums : matrix) {
            System.out.print(nums + " ");
        }
    }

    private static void solution(int numOfAllPlayers, int numOfQuickPlayers, char[] namesOfQuickPlayers, int numOfGames,
            int[] numOfMovesPerGame) {
        char[] peoples = new char[numOfAllPlayers];
        for (int i = 65; i < 65 + numOfAllPlayers; i++) {
            peoples[i - 65] = (char) i;
        }
        int[] count = new int[numOfAllPlayers];
        count[0] += 1;
        LinkedList<Character> results = new LinkedList<>();
        for (int i = 1; i < numOfAllPlayers; i++) {
            results.add(peoples[i]);
        }
        PrintLink(results);
        for (int i = 0; i < numOfGames; i++) {
            int velocity = numOfMovesPerGame[i];
            int N = numOfAllPlayers;
            System.out.println((3 + velocity) % N);
            int start = 0;
            // System.out.println();
            // System.out.println(3 + velocity % (N - 1));
        }
    }

    private static class InputData {
        int numOfAllPlayers;
        int numOfQuickPlayers;
        char[] namesOfQuickPlayers;
        int numOfGames;
        int[] numOfMovesPerGame;
    }

    private static InputData processStdin() {
        InputData inputData = new InputData();

        try (Scanner scanner = new Scanner(System.in)) {
            inputData.numOfAllPlayers = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));

            inputData.numOfQuickPlayers = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));
            inputData.namesOfQuickPlayers = new char[inputData.numOfQuickPlayers];
            System.arraycopy(scanner.nextLine().trim().replaceAll("\\s+", "").toCharArray(), 0,
                    inputData.namesOfQuickPlayers, 0, inputData.numOfQuickPlayers);

            inputData.numOfGames = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));
            inputData.numOfMovesPerGame = new int[inputData.numOfGames];
            String[] buf = scanner.nextLine().trim().replaceAll("\\s+", " ").split(" ");
            for (int i = 0; i < inputData.numOfGames; i++) {
                inputData.numOfMovesPerGame[i] = Integer.parseInt(buf[i]);
            }
        } catch (Exception e) {
            throw e;
        }

        return inputData;
    }

    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        InputData inputData = processStdin();

        solution(inputData.numOfAllPlayers, inputData.numOfQuickPlayers, inputData.namesOfQuickPlayers,
                inputData.numOfGames, inputData.numOfMovesPerGame);
    }
}