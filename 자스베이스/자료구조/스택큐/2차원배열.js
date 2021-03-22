const makeArray = (row, col, value) => {
  return Array.from(Array(row), () => Array(col).fill(value));
};
