const lower_bound = (nums, M) => {
  let start = 0;
  let end = nums.length - 1;
  while (start < end) {
    let mid = parseInt((start + end) / 2);
    if (nums[mid] < M) {
      start = mid + 1;
    } else {
      end = mid;
    }
  }
  return start;
};
console.log(lower_bound([1, 2, 3, 4, 4, 4, 5, 6, 7, 8], 4));
