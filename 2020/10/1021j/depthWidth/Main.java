import java.io.FileInputStream;

import java.util.*;

class Node {
    int left, right;
    public int order, depth;

    Node(int left, int right) {
        this.left = left;
        this.right = right;
    }
}

public class Main {
    static Node[] tree = new Node[10001];
    static int[] left = new int[10001];
    static int[] right = new int[10001];
    static int[] cnt = new int[10001];
    static int order = 0;

    static void inorder(int node, int depth) {
        if (node == -1)
            return;
        inorder(tree[node].left, depth + 1);
        tree[node].order = ++order;
        tree[node].depth = depth;
        inorder(tree[node].right, depth + 1);
    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./depthWidth.txt"));
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            int z = sc.nextInt();
            tree[x] = new Node(y, z);
            if (y != -1)
                cnt[y] += 1;
            if (z != -1)
                cnt[z] += 1;
        }
        int root = 0;
        for (int i = 1; i <= n; i++) {
            if (cnt[i] == 0) {
                root = i;
            }
        }
        inorder(root, 1);
        int maxdepth = 0;
        for (int i = 1; i <= n; i++) {
            int depth = tree[i].depth;
            int order = tree[i].order;
            if (left[depth] == 0) {
                left[depth] = order;
            } else {
                left[depth] = Math.min(left[depth], order);
            }
            right[depth] = Math.max(right[depth], order);
            maxdepth = Math.max(maxdepth, depth);
        }
        int ans = 0;
        int ans_level = 0;
        for (int i = 1; i <= maxdepth; i++) {
            if (ans < right[i] - left[i] + 1) {
                ans = right[i] - left[i] + 1;
                ans_level = i;
            }
        }
        System.out.println(ans_level + " " + ans);
    }
}