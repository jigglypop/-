function solution(nums) {
  var N = nums.length;
  var results = [];

  const comb = (k, start, choice) => {
    if (k === 3) {
      results.push(choice.reduce((a, b) => (a += b), 0));
    }
    for (let i = start; i < nums.length; i++) {
      choice.push(nums[i]);
      comb(k + 1, i + 1, choice);
      choice.pop();
    }
  };

  const isPrime = (num) => {
    if (num < 2) return true;
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) return false;
    }
    return true;
  };

  comb(0, 0, []);
  let count = 0;
  for (let result of results) {
    if (isPrime(result)) count++;
  }
  return count;
}

// console.log(solution([1, 2, 3, 4]));
console.log(solution([1, 2, 7, 6, 4]));
