import java.util.*;

public class ex {
    public static void main(String[] args) {
        Integer[] intArray = new Integer[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        List numberList = Arrays.asList(intArray);
        numberList.forEach(System.out::println);
    }
}
