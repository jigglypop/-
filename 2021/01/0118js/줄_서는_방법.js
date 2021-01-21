// const next_permutation = (nums) => {
//   if (nums.length <= 1) return;
//   let j;
//   for (let i = nums.length - 2; i >= 0; i--) {
//     if (nums[i] < nums[i + 1]) {
//       j = i;
//       break;
//     }
//   }
//   for (let i = nums.length - 1; i > j; i--) {
//     if (nums[i] > nums[j]) {
//       [nums[i], nums[j]] = [nums[j], nums[i]];
//       let temp = nums.splice(j + 1);
//       temp.sort((a, b) => a - b);
//       nums.push(...temp);
//       return;
//     }
//   }
//   nums.sort((a, b) => a - b);
//   return nums;
// };

function solution(n, k) {
  var answer = [];
  let arr = [];
  for (let i = 1; i <= n; i++) arr.push(i);
  let fac = arr.reduce((acc, val) => acc * val, 1);
  k--;
  while (answer.length !== n) {
    fac = fac / arr.length;
    let temp = arr[Math.floor(k / fac)];
    answer.push(temp);
    k = k % fac;
    arr = arr.filter((e) => e !== temp);
  }
  return answer;
}
console.log(solution(3, 5));
