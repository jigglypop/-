import java.util.*;
import java.io.*;

public class Main {

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            String[] splited = str.split(",");
            int sums = 0;
            for (String s : splited) {
                int temp = Integer.parseInt(s);
                sums += temp;
            }
            bw.write(sums + "\n");
        }
        bw.flush();
    }
}
