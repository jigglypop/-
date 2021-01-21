function solution(s) {
  let stack = [];
  for (let i = 0; i < s.length; i++) {
    if (!stack.length) {
      stack.push(s.charAt(i));
    } else {
      if (stack[stack.length - 1] === "(") {
        if (s.charAt(i) === ")") {
          stack.pop();
        } else {
          stack.push(s.charAt(i));
        }
      } else {
        stack.push(s.charAt(i));
      }
    }
  }
  if (!stack.length) {
    return true;
  } else {
    return false;
  }
}

// function is_pair(s){
//   var l = 0, r = 0
//   for (var i = 0; i < s.length; ++i) {
//     if (s[i] == '(') {
//       ++l
//     } else if (s[i] == ')') {
//       if (l == 0) return false
//       else --l
//     }
//   }
//   return l == 0
// }

// function is_pair(s){
//   var result = s.match(/(\(|\))/g);
//   return result[0] == '(' && result.length % 2 == 0 ? true : false
// }
console.log(solution("()()"));
