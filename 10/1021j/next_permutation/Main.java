import java.io.FileInputStream;
import java.util.*;

public class Main {
    public static boolean next_permutation(int[] nums) {
        int i = nums.length - 1;
        while (i > 0 && nums[i] <= nums[i - 1]) {
            i -= 1;
        }
        if (i <= 0) {
            return false;
        }
        int j = nums.length - 1;
        while (nums[j] <= nums[i - 1]) {
            j -= 1;
        }

        int temp = nums[i - 1];
        nums[i - 1] = nums[j];
        nums[j] = temp;

        j = nums.length - 1;
        while (i < j) {
            temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i += 1;
            j -= 1;
        }
        return true;
    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] nums = new int[N];
        for (int i = 0; i < N; i++) {
            nums[i] = sc.nextInt();
        }
        if (next_permutation(nums)) {
            for (int i = 0; i < N; i++) {
                System.out.print(nums[i] + " ");
            }
            System.out.println();
        } else {
            System.out.println("-1");
        }

    }
}
