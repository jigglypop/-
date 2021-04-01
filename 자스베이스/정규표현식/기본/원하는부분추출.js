const text = "From chlgmltn101@naver.com Sat Jan  5 09:14:16 2019";
const string1 = /\S+@\S+/g.exec(text);
// 2. 소괄호
const string2 = /From (\S+@\S+)/g.exec(text);
// 이메일 호스트 출력
const string3 = /@([^ ]+)/g.exec(text);
console.log(string1[0]);
console.log(string2[0]);
console.log(string3[0]);
