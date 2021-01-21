// function solution(participant, completion) {
//   participant.sort();
//   completion.sort();
//   for (let i = 0; i < completion.length; i++) {
//     if (completion[i] !== participant[i]) {
//       return participant[i];
//     }
//   }
//   return participant[participant.length - 1];
// }
var solution = (_, $) =>
  _.find(
    (_) => !$[_]--,
    $.map((_) => ($[_] = ($[_] | 0) + 1))
  );

console.log(solution(["leo", "kiki", "eden"], ["eden", "kiki"]));

// const setA = new Set([1,2,3,4,5,6,7,8]); // array => set 으로 변환 (알아서 중복제거 됨)
// const setB = new Set([3,4,5,6,7]);

// const union = new Set([...setA, ...setB]); // set => array spread syntax 사용
// const intersection = new Set([...setA].filter(x => setB.has(x))); // 둘 다 있는 것들을 솎아낸다.
// const difference1 = new Set([...setA].filter(x => !setB.has(x))); // set1 - set2
// const difference2 = new Set([...setB].filter(x => !setA.has(x))); // set2 - set1
// const symmetricDifference = new Set([...difference1, ...difference2]); // union - intersection

// const isSuperSet = function (superset, subset) { // check if left set(superset) is a superset of right set(subset)
//   for (let element of subset) if (!superset.has(element)) false; // 한 번이라도 superset으로 들어온 집합이 subset으로 들어온 집합의 값을 가지고 있지 않다면 => false
//   return true;
// }
