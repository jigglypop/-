function solution(user_id, banned_id) {
  var banned_match = banned_id.map((x) =>
    x
      .split("")
      .map((x) => x.replace("*", `[\\w]`))
      .join("")
  );
  var banned_length = banned_id.map((x) => x.length);
  let result = [];
  for (let i = 0; i < banned_match.length; i++) {
    let temp = [];
    for (let user of user_id) {
      if (user.match(banned_match[i]) && banned_length[i] === user.length) {
        temp.push(user);
      }
    }
    result.push(temp);
  }
  var result_set = new Set();
  const go = (k, choice) => {
    if (k === banned_match.length) {
      let temp = [];
      for (let i = 0; i < choice.length; i++) {
        let j = choice[i];
        temp.push(result[i][j]);
      }
      let temp_set = new Set(temp);
      if ([...temp_set].length === choice.length) {
        result_set.add(temp.sort().join(", "));
      }
      return;
    }
    for (let i = 0; i < result[k].length; i++) {
      if (choice.includes(result[k][i])) continue;
      choice.push(i);
      go(k + 1, choice);
      choice.pop();
    }
  };
  go(0, []);
  return [...result_set].length;
}
console.log(
  solution(
    ["frodo", "fradi", "crodo", "abc123", "frodoc"],
    ["fr*d*", "*rodo", "******", "******"]
  )
);
