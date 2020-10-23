import java.util.*;

public class Main {
    public class Print<T> {
        public T Type;
        public List<T> list;

        public void print() {
            for (T i : list) {
                System.out.print(i + "");
            }
            System.out.println();

        }
    }

    public static void main(String args[]) throws Exception {
        List<String> list = Arrays.asList("1", "2", "3");
        Print<String> list2;
    }
}
