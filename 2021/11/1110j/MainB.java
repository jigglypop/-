import java.io.*;
import java.util.*;

public class MainB {
    static StringTokenizer st;
    static int N, n;
    static ArrayList<String> Q;

    static void go(int k, String s) {
        if (k == n) {
            Q.add(s);
            return;
        }
        k++;
        go(k, s + " " + k);
        go(k, s + "+" + k);
        go(k, s + "-" + k);
    }
    public static void main(String[] args) throws Exception{
        System.setIn(new FileInputStream("./7490.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            Q = new ArrayList<>();
            StringBuilder sb = new StringBuilder();
            go(1, "1");
            ArrayList<String> L = new ArrayList<>();
            for (String s : Q) {
                String temp = s.replace(" ", "").replace("+", " +").replace("-", " -");
                String[] temp_list = temp.split(" ");
                int temp_value = 0;
                for (String t : temp_list) {
                    temp_value += Integer.parseInt(t);
                }
                if (temp_value == 0)
                    sb.append(s).append("\n");
            }
            System.out.println(sb);
        }
    }
}
