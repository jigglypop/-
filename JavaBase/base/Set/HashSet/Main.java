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

    }
}
