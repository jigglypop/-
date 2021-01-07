function solution(skill, skill_trees) {
  let count = 0;
  let table = {};
  for (let i = 0; i < skill.length; i++) {
    table[skill.charAt(i)] = i;
  }
  for (let tree of skill_trees) {
    let index = 0;
    let flag = true;
    for (let i = 0; i < tree.length; i++) {
      let now = table[tree.charAt(i)];
      if (now === undefined) continue;
      if (now === index) {
        index++;
      } else {
        flag = false;
        break;
      }
    }
    if (flag) count++;
  }
  return count;
}
console.log(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]));
