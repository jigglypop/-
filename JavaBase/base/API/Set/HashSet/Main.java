import java.util.*;

public class Main {

    public static void main(String args[]) throws Exception {
        Set<String> words = new HashSet<String>();

        // 1. add
        words.add("a");
        words.add("b");
        words.add("c");
        words.add("d");
        words.add("e");

        // 2. size
        System.out.println(words.size());

        // 3. iterator
        Iterator<String> iterator = words.iterator();
        while (iterator.hasNext()) {
            String i = iterator.next();
            System.out.printf("%s ", i);
        }
        System.out.println();
        // 4. remove
        words.remove("a");
        words.remove("b");
        for (String word : words) {
            System.out.printf("%s ", word);
        }
        System.out.println();

        //

        Set<Integer> S1 = new HashSet<>();
        Set<Integer> S2 = new HashSet<>();
        Set<Integer> S3 = new HashSet<>();

        S1.add(1);
        S1.add(2);
        S1.add(3);
        S1.add(4);

        S2.add(3);
        S2.add(4);
        S2.add(5);
        S2.add(6);

        S3.add(1);
        S3.add(2);

        // 1. addAll
        S1.addAll(S2);
        System.out.println(S1);
        // 2. retainAll
        S1.retainAll(S2);
        System.out.println(S1);

        // 3. containsAll
        System.out.println(S1.containsAll(S2));

        // 4. removeAll
        S1.removeAll(S2);
        System.out.println(S1);

    }
}
