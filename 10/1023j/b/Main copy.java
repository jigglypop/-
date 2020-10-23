// import java.io.*;
// import java.util.*;

// public class Main {
// public static int divide(int x, int e) {
// if (x % e == 0) {
// return e;
// } else {
// return x % e;
// }
// }

// public static void main(String args[]) throws Exception {
// System.setIn(new FileInputStream("./input.txt"));
// BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
// StringTokenizer st = new StringTokenizer(br.readLine());
// int E = Integer.parseInt(st.nextToken());
// int S = Integer.parseInt(st.nextToken());
// int M = Integer.parseInt(st.nextToken());
// for (int i = 1; i <= 15 * 28 * 19 + 1; i++) {
// int e = divide(i, 15);
// int s = divide(i, 28);
// int m = divide(i, 19);
// if (e == E && s == S && m == M) {
// System.out.println(i);
// break;
// }
// }
// }
// }
