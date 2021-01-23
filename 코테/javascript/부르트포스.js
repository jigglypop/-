//피보나치
const fibo = (num) => {
  let memo = [0, 1];
  for (var i = 2; i < num + 1; i++) {
    memo[i] = (memo[i - 1] + memo[i - 2]) % 1234567;
  }
  return memo[num];
};

// 하노이
const hanoi = (n, from, to) => {
  const by = 6 - from - to;
  if (n === 1) {
    answer.push([from, to]);
  } else {
    hanoi(n - 1, from, by);
    answer.push([from, to]);
    hanoi(n - 1, by, to);
  }
};
// 소수찾기
const isPrime = (number) => {
  if (number < 2) return false;
  if (number === 2) return true;
  for (let i = 2; i <= Math.sqrt(number); i++) {
    if (number % i === 0) return false;
  }
  return true;
};
// 에라토스테네스
const eratos = (n) => {
  let primes = Array(n + 1).fill(false);
  primes[1] = true;
  for (let i = 2; i <= n; i++) {
    if (primes[i] === false) {
      for (let j = i + i; j <= n; j += i) {
        primes[j] = true;
      }
    }
  }
  for (let i = 2; i <= n; i++) {
    if (primes[i] === false) {
      answer += 1;
    }
  }
  return primes;
};
// 최대공약수, 최소공배수
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

// 다음순열
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
// 부분집합
const subset = (N, n, numbers) => {
  let result = [];
  for (let i = 0; i < N; i++) {
    let choice = [];
    for (let j = 0; j < n; j++) {
      if (i & (1 << j)) continue;
      choice.push(numbers[j]);
    }
    result.push(choice);
  }
  return result;
};
// 순열
const perm = (k, N, used, choice, numbers) => {
  if (k === N) {
    console.log(choice.join(" "));
    return;
  }
  for (let i = 0; i < numbers.length; i++) {
    if (used & (1 << i)) continue;
    choice.push(numbers[i]);
    perm(k + 1, N, used | (1 << i), choice, numbers);
    choice.pop();
  }
};

// 조합
const comb = (k, N, start, choice, numbers) => {
  if (k === N) {
    console.log(choice.join(" "));
    return;
  }
  for (let i = start; i < numbers.length; i++) {
    choice.push(numbers[i]);
    comb(k + 1, N, i + 1, choice, numbers);
    choice.pop();
  }
};

// 이분탐색
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
const upper_bound = (nums, M) => {
  let start = 0;
  let end = nums.length - 1;
  while (start < end) {
    let mid = parseInt((start + end) / 2);
    if (nums[mid] <= M) {
      start = mid + 1;
    } else {
      end = mid;
    }
  }
  return start;
};

// 힙
class MaxHeap {
  heap = [0];

  swap(a, b) {
    [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
  }
  push(v) {
    this.heap.push(v);
    let i = this.heap.length - 1;
    while (i > 1 && this.heap[Math.floor(i / 2)] < this.heap[i]) {
      this.swap(i, Math.floor(i / 2));
      i = Math.floor(i / 2);
    }
  }

  pop() {
    if (this.heap.length <= 1) return 0;
    let x = this.heap[1];
    this.heap[1] = this.heap[this.heap.length - 1];
    this.heap.pop();
    let i = 1;
    while (i * 2 < this.heap.length) {
      let max = this.heap[i * 2];
      let _i = i * 2;
      if (i * 2 + 1 < this.heap.length && max < this.heap[i * 2 + 1]) {
        max = this.heap[i * 2 + 1];
        _i = i * 2 + 1;
      }
      if (this.heap[i] > max) break;
      this.swap(i, _i);
      i = _i;
    }
    return x;
  }
}
class MinHeap {
  heap = [0];

  swap(a, b) {
    [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
  }
  push(v) {
    this.heap.push(v);
    let i = this.heap.length - 1;
    while (i > 1 && this.heap[Math.floor(i / 2)] > this.heap[i]) {
      this.swap(i, Math.floor(i / 2));
      i = Math.floor(i / 2);
    }
  }

  pop() {
    if (this.heap.length <= 1) return 0;
    let x = this.heap[1];
    this.heap[1] = this.heap[this.heap.length - 1];
    this.heap.pop();
    let i = 1;
    while (i * 2 < this.heap.length) {
      let max = this.heap[i * 2];
      let _i = i * 2;
      if (i * 2 + 1 < this.heap.length && max > this.heap[i * 2 + 1]) {
        max = this.heap[i * 2 + 1];
        _i = i * 2 + 1;
      }
      if (this.heap[i] < max) break;
      this.swap(i, _i);
      i = _i;
    }
    return x;
  }
}

function solution(num) {
  return fibo(num);
}
console.log(solution(3));
