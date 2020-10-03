public class LowerBound {
    public static void main(String[] args) {
        int[] nums = { 1, 2, 3, 4, 4, 4, 5, 6, 7, 8 };
        int start = 0;
        int end = nums.length - 1;
        int M = 4;
        while (start <= end) {
            int mid = (start + end) / 2;
            int temp = nums[mid];
            if (temp >= M) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        System.out.print(end + 1);
    }
}
