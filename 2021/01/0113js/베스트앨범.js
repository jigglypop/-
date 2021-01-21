function solution(genres, plays) {
  var answer = [];
  let table = {};
  let genre_sets = [];
  for (let i = 0; i < genres.length; i++) {
    if (table[genres[i]]) {
      table[genres[i]].push([i, parseInt(plays[i])]);
    } else {
      genre_sets.push(genres[i]);
      table[genres[i]] = [[i, parseInt(plays[i])]];
    }
  }
  let orders = [];
  for (let genre of genre_sets) {
    orders.push([genre, table[genre].reduce((acc, cur) => (acc += cur[1]), 0)]);
  }
  orders.sort((a, b) => b[1] - a[1]);
  for (let order of orders) {
    answer = answer.concat(
      table[order[0]]
        .sort((a, b) => b[1] - a[1])
        .slice(0, 2)
        .map((x) => (x = x[0]))
    );
  }
  return answer;
}
console.log(
  solution(
    ["classic", "pop", "classic", "classic", "pop"],
    [500, 600, 150, 800, 2500]
  )
);
