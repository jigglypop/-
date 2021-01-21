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
const numbers = [1, 2, 3];
console.log(subset(1 << numbers.length, numbers.length, numbers));
