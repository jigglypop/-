const words = "aaabccc";
for (let word of words.match(/(\w)\1+/g)) {
  console.log(word);
}
