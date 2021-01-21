const next_permutation = (nums) => {
  if (nums.length <= 1) return;
  let j;
  for (let i = nums.length - 2; i >= 0; i--) {
    if (nums[i] < nums[i + 1]) {
      j = i;
      break;
    }
  }
  for (let i = nums.length - 1; i > j; i--) {
    if (nums[i] > nums[j]) {
      [nums[i], nums[j]] = [nums[j], nums[i]];
      let temp = nums.splice(j + 1);
      temp.sort((a, b) => a - b);
      nums.push(...temp);
      return;
    }
  }
  nums.sort((a, b) => a - b);
  return nums;
};
