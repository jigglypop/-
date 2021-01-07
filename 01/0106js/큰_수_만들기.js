function solution(number, k) {
  var b = [];
  for (var i = 0; i < number.length; i++) {
    var c = number[i];
    while (k > 0 && b.length > 0 && b[b.length - 1] < c) {
      b.pop();
      k--;
    }
    b.push(c);
  }
  b.splice(b.length - k, k);
  return b.join("");
}
console.log(solution("4177252841", 4));
