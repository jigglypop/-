public class Main {
    public static void main(String[] args) {
        int[][] di = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, -1 } };
        for (int[] dir : di) {
            int dy = dir[0];
            int dx = dir[1];
            System.out.println(dy + " " + dx);
        }
    }
}
