function solution(phone_number) {
  return (
    "*".repeat(phone_number.length - 4) +
    phone_number.substr(phone_number.length - 4, phone_number.length)
  );
}
console.log(solution("01033334444"));
