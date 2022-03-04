import java.util.*;
import java.util.regex.*;

public class Main1 {
    public static ArrayList<String> Regex(String p, String text) {
        Pattern pattern = Pattern.compile(p);
        Matcher matcher = pattern.matcher(text);
        ArrayList<String> result = new ArrayList<>();
        while (matcher.find()) {
            result.add(matcher.group(0));
        }
        return result;
    }

    public static void main(String args[]) {

        // 1. ^ $
        ArrayList<String> words = Regex("He", "HeHeHe");
        for (String word : words) {
            System.out.printf("%s ", word);
        }
        // printRegex("^Hello", "hi,Hello,world");
        // printRegex("world$", "Hello, world");

        // // 2. |
        // printRegex("hello|world", "hello");

        // // 3. * +
        // printRegex("[0-9]+", "1234");
        // printRegex("[0-9]*", "1234");
        // printRegex("[0-9]*", "abcd");

        // printRegex("a*b", "b");
        // printRegex("a+b", "b");
        // printRegex("a*b", "aab");
        // printRegex("a+b", "aab");

        // // 4. ? .
        // printRegex("H?", "H");
        // printRegex("H?", "Hi");
        // printRegex("H.", "Hi");

        // // 5. {}
        // printRegex("h{3}", "hhhello");
        // printRegex("(hello){3}", "hellohellohello");
        // printRegex("[0-9]{3}-[0-9]{3}-[0-9]{4}", "010-101-0101");

        // // 6. [range]+
        // printRegex("[a-zA-Z0-9]+", "Hello1234");
        // printRegex("[A-Z0-9]+", "hello");

        // // 7. [^range]*
        // printRegex("[^A-Z]*", "hello");
        // printRegex("[^A-Z]+", "hello");

        // // 8. [range]*$
        // printRegex("[0-9]+$", "Hello1234");

        // // 9. \
        // printRegex("[a-zA-Z0-9\s]+", "Hello 1234");

        // // 10. group
        // printRegex("([0-9]+) ([0-9]+)", "10 123");

    }
}
