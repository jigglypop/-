import java.io.*;
import java.util.*;

public class Default {
    static StringTokenizer st;
    static int N;
    public static void main(String[] args) throws Exception{
        System.setIn(new FileInputStream("./7490.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        String s = "1-2";
        String temp = "-2";
        temp += 3;
        int k = Integer.parseInt(temp) + 1;
        System.out.println(k);
    }
}
