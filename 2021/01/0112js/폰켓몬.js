function solution(nums) {
  var answer = 0;
  var table = {};
  var N = nums.length / 2;
  var len = 0;
  for (let i = 0; i < nums.length; i++) {
    if (table[nums[i]] === undefined) {
      table[nums[i]] = 1;
      len++;
    } else {
      table[nums[i]]++;
    }
  }
  answer = Math.min(N, Object.keys(table).length);
  return answer;
}
console.log(solution([3, 1, 2, 3]));
