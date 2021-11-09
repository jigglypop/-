import java.io.*;
import java.util.*;

public class MainA {
    static StringTokenizer st;
    static int N;
    public static void main(String[] args) throws Exception{
        System.setIn(new FileInputStream("./2231.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        for(int i = 0; i < N; i++) {
            int number = i;
            int sum = 0;	
            while(number != 0) {
                sum += number % 10;	
                number /= 10;
            }
            if(sum + i == N) {
                System.out.println(i);
                break;
            }
        }	
    }
}
