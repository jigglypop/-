const quicksort = (nums) => {
  if (nums.length <= 1) return nums;
  let pivot = nums[0];
  let left = [];
  let right = [];
  for (let i = 1; i < nums.length; i++) {
    nums[i] < pivot ? left.push(nums[i]) : right.push(nums[i]);
  }
  return quicksort(left).concat(pivot, quicksort(right));
};

console.log(quicksort([3, 1, 2, 5, 4]));
