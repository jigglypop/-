import java.io.*;
import java.util.*;

public class MainE {

    static StringTokenizer st;
    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("./10546.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        Map<String, Integer> map = new HashMap<>();

        for (int i = 0; i < N * 2 - 1; i++) {
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            if (map.containsKey(name)) {
                map.replace(name, map.get(name) + 1);
            } else {
                map.put(name, 1);
            }
        }

        for (String key : map.keySet()) {
            if (map.get(key) % 2 == 1) {
                System.out.println(key);
                break;
            }
		}
    }
}
