function solution(nums) {
  const gcd = (a, b) => {
    if (a % b === 0) {
      return b;
    }
    return gcd(b, a % b);
  };
  const lcm = (a, b) => {
    const GCD = gcd(a, b);
    return (a / GCD) * (b / GCD) * GCD;
  };
  let LCM = nums[0];
  for (let i = 1; i < nums.length; i++) {
    LCM = lcm(LCM, nums[i]);
  }
  return LCM;
}
console.log(solution([1, 2, 3]));
