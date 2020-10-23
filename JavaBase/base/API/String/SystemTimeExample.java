public class SystemTimeExample {
    public static void main(String[] args) {
        long time1 = System.nanoTime();
        int sum = 0;
        for (int i = 0; i <= 1000000; i++) {
            sum += i;
        }
        long time2 = System.nanoTime();
        System.out.println(sum);
        System.out.println(time2 - time1);
        long time3 = System.nanoTime();
        int sum2 = 0;
        for (int i = 0; i <= 100; i++) {
            sum2 += i;
        }
        long time4 = System.nanoTime();
        System.out.println(sum2);
        System.out.println(time4 - time3);
    }
}
