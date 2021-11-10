import java.io.*;
import java.util.*;

public class MainE {
    static StringTokenizer st;
    static int N;
    public static void main(String[] args) throws Exception{
        System.setIn(new FileInputStream("./2675.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            String s = st.nextToken();
            String temp = "";
            for (int j = 0; j < s.length(); j++) {
                char t = s.charAt(j);
                for (int k = 0; k < n; k++) {
                    temp += t;
                }
            }
            sb.append(temp).append("\n");
        }
        System.out.println(sb);
    }
}
