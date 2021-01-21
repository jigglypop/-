
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
//
//     Pair(int y, int x) {
//         this.y = y;
//         this.x = x;
//     }
// }
//
//
// 3. Node
//
// class Node {
//     int left, right;
//
//     Node(int left, int right) {
//         this.left = left;
//         this.right = right;
//     }
// }
//
// 4. kruskal
//
// class Edge implements Comparable<Edge> {
//     int from;
//     int to;
//     int cost;
//     Edge(int from, int to, int cost) {
//         this.from = from;
//         this.to = to;
//         this.cost = cost;
//     }
//     @Override
//     public int compareTo(Edge that) {
//         return Integer.compare(this.cost, that.cost);
//     }
// }
// static int[] parent;
// public static int find(int x) {
//     if (parent[x] == x) {
//         return x;
//     }
//     return parent[x] = find(parent[x]);
// }
// public static boolean union(int a, int b) {
//     int x = find(a);
//     int y = find(b);
//     if (x != y) {
//         parent[y] = x;
//         return true;
//     }
//     return false;
// }
// public static long kruskal(PriorityQueue<Edge> pq, int V) {
//     parent = new int[V + 1];
//     for (int i = 1; i <= V; i++) {
//         parent[i] = i;
//     }
//     long result = 0;
//     while (V > 1) {
//         Edge p = pq.remove();
//         if (union(p.from, p.to)) {
//             result += p.cost;
//             V--;
//         }
//     }
//     return result;
// }

// 5. lca
// static int[] parent;
// static int[] depth;

// public static int lca(int u, int v) {
//     if (depth[u] < depth[v]) {
//         int temp = u;
//         u = v;
//         v = temp;
//     }
//     while (depth[u] != depth[v]) {
//         u = parent[u];
//     }
//     while (u != v) {
//         u = parent[u];
//         v = parent[v];
//     }
//     return u;
// }
// parent = new int[N + 1];
// depth = new int[N + 1];
// depth[1] = 0;
// parent[1] = 1;
// Queue<Integer> Q = new LinkedList<Integer>();
// boolean[] check = new boolean[N + 1];
// check[1] = true;
// Q.add(1);
// while (!Q.isEmpty()) {
//     int u = Q.remove();
//     for (int v : tree[u]) {
//         if (!check[v]) {
//             depth[v] = depth[u] + 1;
//             check[v] = true;
//             parent[v] = u;
//             Q.add(v);
//         }
//     }
// }

import java.util.*;
import java.io.*;

class HighTreeMain {

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