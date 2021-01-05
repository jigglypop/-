import java.io.FileInputStream;
import java.util.*;

public class Main {

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./parent.txt"));
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        ArrayList<Integer>[] tree = new ArrayList[N + 1];
        for (int i = 1; i <= N; i++) {
            tree[i] = new ArrayList<Integer>();
        }
        for (int i = 0; i < N - 1; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            tree[u].add(v);
            tree[v].add(u);
        }
        boolean[] check = new boolean[N + 1];
        int[] parent = new int[N + 1];
        Queue<Integer> Q = new LinkedList<Integer>();
        Q.add(1);
        check[1] = true;
        while (!Q.isEmpty()) {
            int x = Q.remove();
            for (int y : tree[x]) {
                if (check[y] == false) {
                    check[x] = true;
                    parent[y] = x;
                    Q.add(y);
                }
            }
        }
        for (int i = 2; i <= N; i++) {
            System.out.println(parent[i]);
        }
    }
}
