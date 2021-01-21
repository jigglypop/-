public class ThreadExample {
    public static Runnable getRunnable() {
        return () -> System.out.println("Hello World");
    }

    public static void main(String[] args) {
        // Thread thread = new Thread(new Runnable() {
        // @Override
        // public void run() {
        // System.out.println("Hello World");
        // }
        // });
        // thread.start();

        // lambda 1

        // Thread thread = new Thread(() -> {
        // System.out.println("Hello World");
        // });
        // thread.start();

        // lambda 2

        // Runnable runImpl = () -> {
        // System.out.println("Hello World");
        // };
        // Thread thread = new Thread(runImpl);
        // thread.start();

        // lambda 3

        Runnable runImpl = getRunnable();
        Thread thread = new Thread(runImpl);
        thread.start();
    }
}
