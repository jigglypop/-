const calc_table = {
  "*": (a, b) => {
    return a * b;
  },
  "-": (a, b) => {
    return a - b;
  },
  "+": (a, b) => {
    return a + b;
  },
};
console.log(calc_table["+"](1, 2));
