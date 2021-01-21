import java.util.*;
import java.util.stream.IntStream;

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
        System.out.println(words.contains("a"));
        System.out.println(words.get(1));

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
        for (String i : words) {
            System.out.printf("%s ", i);
        }
        System.out.println();

        // 4. forEach
        List<String> list = new ArrayList<>();
        list.add("1");
        list.add("2");
        list.add("3");
        System.out.println(list);
        list.forEach((a) -> {
            System.out.print(a + " ");
        });
        System.out.println(list);
        // 5. String -> int
        list.forEach((a) -> {
            Integer.parseInt(a);
        });

        // 6. sum
        List<Integer> list2 = Arrays.asList(6, 7, 8, 9, 10);
        int list2Stream = IntStream.of(12, 3).sum();
        System.out.println(list2Stream);

    }
}
