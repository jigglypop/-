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
  const mid = nums.length / 2;
  if (nums.length < 2) {
    return nums;
  }
  const left = nums.splice(0, mid);
  const right = nums;
  return merge(mergesort(left), mergesort(right));
};
console.log(mergesort([3, 1, 2, 5, 4]));
const arr1 = Array.from(Array(4), () => Array(4).fill(1));
console.log(arr1);
