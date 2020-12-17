const merge = (left, right) => {
  let arr = [];
  while (left.length && right.length) {
    if (left[0] < right[0]) {
      arr.push(left.shift());
    } else {
      arr.push(right.shift());
    }
  }
  return [...arr, ...left, ...right];
};

const mergesort = (nums) => {
  const half = nums.length / 2;
  if (nums.length < 2) {
    return nums;
  }
  const left = nums.splice(0, half);
  const right = nums;
  return merge(mergesort(left), mergesort(right));
};
console.log(mergesort([3, 1, 2, 5, 4]));
