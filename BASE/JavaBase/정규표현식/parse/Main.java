import java.util.regex.*;

public class Main {
    public static void printRegex(String p, String text) {
        Pattern pattern = Pattern.compile(p);
        Matcher matcher = pattern.matcher(text);
        while (matcher.find()) {
            System.out.printf("%s ", matcher.group(0));
        }
        System.out.println();
    }

    public static void main(String args[]) {

        String str = "hello";
        String str2 = "hi";
        String str4 = "hello";
        System.out.println(str.equals(str2));
        System.out.println(str.equals(str4));

        String str5 = "hello";
        System.out.println(str5);
        String str6 = str5.replace("ello", "i");
        System.out.println(str6);

        String ssn = "880815-1234567";
        String firstNum = ssn.substring(0, 6);
        String secondNum = ssn.substring(7);
        System.out.println(firstNum);
        System.out.println(secondNum);

        String original = "Java Programming";
        String lowerCase = original.toLowerCase();
        String upperCase = original.toUpperCase();
        System.out.println(lowerCase);
        System.out.println(upperCase);

        String oldStr = "   Java Programming   ";
        String newStr = oldStr.trim();
        System.out.println(newStr);

        String str10 = String.valueOf(10);
        String str20 = String.valueOf(10.5);
        String str30 = String.valueOf(true);
        System.out.println(str10);
        System.out.println(str20);
        System.out.println(str30);

    }
}
