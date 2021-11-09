import java.io.*;
import java.util.*;

public class Default {
    static StringTokenizer st;
    static int N;
    public static void main(String[] args) throws Exception{
        System.setIn(new FileInputStream("./2675.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        System.out.println(N);
    }
}
