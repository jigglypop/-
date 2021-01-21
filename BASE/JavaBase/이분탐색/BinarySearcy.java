
public class BinarySearcy {
    static int binarySearcy(int[] array, int n, int key) {
        int start = 0;
        int end = n - 1;
        while (start <= end) {
            int mid = (start + end) / 2;
            int temp = array[mid];
            if (temp == key) {
                return mid;
            } else if (temp < key) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] array = { 1, 2, 3, 3, 4, 5, 6, 7 };
        System.out.print(binarySearcy(array, array.length, 3));
    }
}
