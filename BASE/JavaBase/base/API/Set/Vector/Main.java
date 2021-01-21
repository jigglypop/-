import java.util.*;

public class Main {

    public static void main(String args[]) throws Exception {
        List<String> words = new ArrayList<String>();

        // 1. add
        words.add("a");
        words.add("b");
        words.add(1, "c");
        words.add("d");
        words.add("e");
        for (String i : words) {
            System.out.printf("%s ", i);
        }
        System.out.println();

        // 2. size
        System.out.println(words.size());

        // 3. get
        String word1 = words.get(1);
        String word2 = words.get(2);
        System.out.println(word1);
        System.out.println(word2);

        // 4. remove
        words.remove(1);
        words.remove("e");
        for (String word : words) {
            System.out.printf("%s ", word);
        }
        System.out.println();

    }
}
