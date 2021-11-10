import java.io.*;
import java.util.*;

public class Main {
    public static int[] next_permutation(int[] nums) {
        int N = nums.length;
        int i = N - 1;
        while (i > 0 && nums[i - 1] >= nums[i]) {
            i -= 1;
        }

        if (i <= 0) {
            return nums;
        }

        int j = N - 1;
        while (nums[j] <= nums[i - 1]) {
            j -= 1;
        }

        int temp = nums[i - 1];
        nums[i - 1] = nums[j];
        nums[j] = temp;

        j = N - 1;
        while (i < j) {
            temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i += 1;
            j -= 1;
        }
        return nums;
    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int[] nums = Arrays.stream(s).mapToInt(Integer::parseInt).toArray();
        int N = nums.length;
        for (int r : nums) {
            System.out.print(r + " ");
        }
        System.out.println();
        int[] result = next_permutation(nums);
        for (int r : result) {
            System.out.print(r + " ");
        }
    }
}
