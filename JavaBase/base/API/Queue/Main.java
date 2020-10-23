import java.util.*;

public class Main {
    public static void Print(Queue<String> Q) {
        for (String q : Q) {
            System.out.print(q + " ");
        }
        System.out.println();
    }

    public static void main(String args[]) throws Exception {
        Queue<String> Q = new LinkedList<String>();
        Q.offer("a");
        Q.offer("b");
        Q.offer("c");
        Print(Q);
        String q = Q.poll();
        System.out.println(q);
        Print(Q);
    }
}
