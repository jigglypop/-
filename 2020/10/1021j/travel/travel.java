import java.io.FileInputStream;
import java.util.*;

class Node {
    int left, right;

    Node(int left, int right) {
        this.left = left;
        this.right = right;
    }
}

public class travel {
    static void preorder(Node[] words, int x) {
        if (x == -1)
            return;
        System.out.print((char) (x + 'A'));
        preorder(words, words[x].left);
        preorder(words, words[x].right);
    }

    static void inorder(Node[] words, int x) {
        if (x == -1)
            return;
        inorder(words, words[x].left);
        System.out.print((char) (x + 'A'));
        inorder(words, words[x].right);
    }

    static void postorder(Node[] words, int x) {
        if (x == -1)
            return;
        postorder(words, words[x].left);
        postorder(words, words[x].right);
        System.out.print((char) (x + 'A'));
    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./travel.txt"));
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        Node[] words = new Node[26];
        for (int i = 0; i < N; i++) {
            int x = sc.next().charAt(0) - 'A';
            char y = sc.next().charAt(0);
            char z = sc.next().charAt(0);
            int left = -1;
            int right = -1;
            if (y != '.') {
                left = y - 'A';
            }
            if (z != '.') {
                right = z - 'A';
            }
            words[x] = new Node(left, right);
        }
        preorder(words, 0);
        System.out.println();
        inorder(words, 0);
        System.out.println();
        postorder(words, 0);
        System.out.println();
    }
}
