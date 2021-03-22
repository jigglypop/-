const upper_bound = (nums, M) => {
  let start = 0;
  let end = nums.length - 1;
  let result = 0;
  while (start <= end) {
    let mid = parseInt((start + end) / 2);
    let temp = nums[mid];
    if (temp <= M) {
      start = mid + 1;
    } else {
      result = mid;
      end = mid - 1;
    }
  }
  return result;
};
console.log(upper_bound([1, 2, 3, 4, 4, 4, 5, 6, 7, 8], 4));
