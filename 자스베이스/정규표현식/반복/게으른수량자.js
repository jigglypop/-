const text =
  "This offer is not available to customers living in <b>AK</b> and <b>HI</b>";

// 방법 1
console.log(text.match(/<[Bb]>.*<\/[Bb]>/g));
// 게으른 수량자
console.log(text.match(/<[Bb]>.*?<\/[Bb]>/g));
