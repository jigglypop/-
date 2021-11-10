import java.io.*;
import java.util.*;

public class MainC {
    static StringTokenizer st;

    public static void main(String[] args) throws Exception{
        System.setIn(new FileInputStream("./11654.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        char N = st.nextToken().charAt(0);
        StringBuilder sb = new StringBuilder();
        sb.append((int) N);
		System.out.println(sb);
	}
}
