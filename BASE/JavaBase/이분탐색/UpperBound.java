public class UpperBound {
    public static void main(String[] args) {
        int[] nums = { 1, 2, 3, 4, 4, 4, 5, 6, 7, 8 };
        int start = 0;
        int end = nums.length - 1;
        int M = 4;
        int result = 0;
        while (start <= end) {
            int mid = (start + end) / 2;
            if (M < nums[mid]) {
                result = mid;
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        System.out.print(result);
    }
}
