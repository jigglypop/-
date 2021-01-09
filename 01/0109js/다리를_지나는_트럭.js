function solution(bridge_length, weight, truck_weights) {
  var answer = 0;
  var crossing = [];
  var finish = [];
  while (truck_weights.length | crossing.length) {
    answer++;
    // console.log(answer, truck_weights, crossing);
    for (let i = 0; i < crossing.length; i++) {
      crossing[i][0] -= 1;
    }
    crossing = crossing.filter((x) => x[0] !== 0);
    let Sum = !crossing.length
      ? 0
      : crossing.reduce((acc, cur) => (acc += cur[1]), 0);
    if (Sum + truck_weights[0] <= weight) {
      let q = truck_weights.shift();
      crossing.push([bridge_length, q]);
    }
  }
  return answer;
}
console.log(solution(2, 10, [7, 4, 5, 6]));
