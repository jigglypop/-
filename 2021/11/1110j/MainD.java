import java.io.*;
import java.util.*;

public class MainD {
    static StringTokenizer st;

    public static void main(String[] args) throws Exception{
        System.setIn(new FileInputStream("./11720.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        String nums = st.nextToken();
        int result = 0;
        for (int i = 0; i < N; i++) {
            result += Integer.parseInt(nums.substring(i, i + 1));
        }
        StringBuilder sb = new StringBuilder();
        sb.append(result);
        System.out.println(sb);
    }
}
