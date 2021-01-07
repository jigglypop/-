function divide(w) {
  let left = 0;
  let right = 0;
  if (w === "") {
    return [w, w];
  }
  for (let i = 0; i < w.length; i++) {
    if (w[i] === ")") {
      right++;
    }
    if (w[i] === "(") {
      left++;
    }
    if (left === right) {
      return [w.slice(0, i + 1), w.slice(i + 1)];
    }
  }
}
function isValid(u) {
  let left = 0;
  let right = 0;
  for (let i = 0; i < u.length; i++) {
    if (u[i] === ")") {
      right++;
    }
    if (u[i] === "(") {
      left++;
    }
    if (left - right < 0) {
      return false;
    }
  }
  return true;
}

//재귀용 함수
function recursion(u, v) {
  if (u === "" && v === "") {
    return "";
  }
  let [u2, v2] = divide(v);
  if (isValid(u)) {
    return u + recursion(u2, v2);
  } else {
    return (
      "(" +
      recursion(u2, v2) +
      ")" +
      u
        .slice(1, -1)
        .split("")
        .map((element) => {
          if (element === "(") {
            return ")";
          } else {
            return "(";
          }
        })
        .join("")
    );
  }
}

function solution(p) {
  let [u, v] = divide(p);
  let result = recursion(u, v);
  return result;
}

// function reverse(str) {
//     return str.slice(1, str.length - 1).split("").map((c) => (c === "(" ? ")" : "(")).join("");
//   }
//   function solution(p) {
//     if (p.length < 1) return "";
//     let balance = 0;
//     let pivot = 0;
//     do { balance += p[pivot++] === "(" ? 1 : -1 } while (balance !== 0);
//     const u = p.slice(0, pivot);
//     const v = solution(p.slice(pivot, p.length));
//     if (u[0] === "(" && u[u.length - 1] == ")") return u + v;
//     else return "(" + v + ")" + reverse(u);
//   }
// console.log(solution(")("));
// console.log(solution("(()())()"));
console.log(solution("()))((()"));
