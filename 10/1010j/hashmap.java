import java.util.HashMap;

public class hashmap {
    public static void main(String[] args) throws Exception {
        System.out.println("hello");
        HashMap<Integer, String> map = new HashMap<Integer, String>();
        // 값 추가
        map.put(1, "a");
        map.put(2, "b");
        System.out.println(map);
        // 값 제거
        map.remove(1);
        System.out.println(map);
        // 값 업데이트
        map.replace(2, "c");
        System.out.println(map);

    }
}
