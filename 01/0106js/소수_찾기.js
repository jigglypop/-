// const perm = (k, N, used, choice, numbers) => {
//   if (k === N) {
//     parseInt(choice.join(""));
//     return;
//   }
//   for (let i = 0; i < numbers.length; i++) {
//     if (used & (1 << i)) continue;
//     choice.push(numbers[i]);
//     perm(k + 1, N, used | (1 << i), choice, numbers);
//     choice.pop();
//   }
// };

const subset = (N, n) => {
  for (let i = 0; i < N; i++) {
    let temp = "";
    for (let j = 0; j < n; j++) {
      if (i & (1 << j)) continue;
      temp += numbers.charAt(j) + "";
    }
    console.log(temp);
  }
};

function isPrime(number) {
  if (number < 2) return false;
  // if (number === 2) return true;
  for (let i = 3; i <= Math.sqrt(number); i++) {
    if (number % i === 0) return false;
  }
  return true;
}
function solution(numbers) {
  var n = numbers.length;
  var results = new Set();
  const perm = (k, N, used, choice) => {
    if (k === N) {
      results.add(parseInt(choice.join("")));
      return;
    }
    for (let i = 0; i < numbers.length; i++) {
      if (used & (1 << i)) continue;
      choice.push(numbers[i]);
      perm(k + 1, N, used | (1 << i), choice);
      choice.pop();
    }
  };
  for (let i = 1; i <= n; i++) {
    perm(0, i, 0, []);
  }
  const results_list = [...results];
  let count = 0;
  for (let number of results_list) {
    if (isPrime(number) && number !== 0) {
      count++;
    }
  }
  return count;
}
console.log(isPrime(2));
console.log(solution("011"));
