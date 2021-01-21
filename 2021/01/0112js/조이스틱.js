function solution(name) {
  const arr = [0];

  const answer = [...name].reduce((answer, s, i) => {
    if (s === "A") {
      if (name[i - 1] != "A") arr.push(continuous(name.substring(i)) - (i - 1));
      return answer + 1;
    }
    return answer + ascii(name, i) + 1;
  }, 0);

  return answer - Math.max(...arr) - 1;
}

function ascii(name, i) {
  const num = name.charCodeAt(i);
  return num > 78 ? 91 - num : num - 65;
}

function continuous(name) {
  let repeat = 0;
  for (let i = 0; i < name.length; i++) {
    if (name[i] != "A") break;
    repeat++;
  }
  return repeat;
}
console.log(solution("JEROEN"));
