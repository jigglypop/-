function solution(numbers, hand) {
  let result = "";
  let keypad = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2],
    0: [3, 1],
  };
  const left_set = new Set([1, 4, 7]);
  const right_set = new Set([3, 6, 9]);

  let left_point = [3, 0];
  let right_point = [3, 2];

  for (let number of numbers) {
    if (left_set.has(number)) {
      result += "L";
      left_point = keypad[number];
    } else if (right_set.has(number)) {
      result += "R";
      right_point = keypad[number];
    } else {
      if (
        Math.abs(left_point[0] - keypad[number][0]) +
          Math.abs(left_point[1] - keypad[number][1]) >
        Math.abs(right_point[0] - keypad[number][0]) +
          Math.abs(right_point[1] - keypad[number][1])
      ) {
        result += "R";
        right_point = keypad[number];
      } else if (
        Math.abs(left_point[0] - keypad[number][0]) +
          Math.abs(left_point[1] - keypad[number][1]) <
        Math.abs(right_point[0] - keypad[number][0]) +
          Math.abs(right_point[1] - keypad[number][1])
      ) {
        result += "L";
        left_point = keypad[number];
      } else {
        if (hand === "left") {
          result += "L";
          left_point = keypad[number];
        } else {
          result += "R";
          right_point = keypad[number];
        }
      }
    }
  }
  return result;
}

console.log(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"));
