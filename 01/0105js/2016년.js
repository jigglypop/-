function solution(a, b) {
  return ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"][
    new Date(`2016,${a},${b}`).getDay()
  ];
}
console.log(solution(5, 24));
