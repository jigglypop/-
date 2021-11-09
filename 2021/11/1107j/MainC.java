import java.io.*;
import java.util.*;

public class MainC {
    static StringTokenizer st;
    public static void main(String[] args) throws Exception{
        System.setIn(new FileInputStream("./1269.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        HashSet<Integer> setA = new HashSet<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < A; i++) {
            setA.add(Integer.parseInt(st.nextToken()));
        }

        st = new StringTokenizer(br.readLine());
        int count = setA.size();
        for (int i = 0; i < B; i++) {
            int temp = Integer.parseInt(st.nextToken());
            if (!setA.contains(temp)) {
                count++;
            } else {
                count--;
            }
        }
        sb.append(count);
        System.out.println(sb);
    }
}
