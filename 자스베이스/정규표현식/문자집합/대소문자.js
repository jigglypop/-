const text = `
    The phrase "regular expression" is often
    abbreviated as RegEx or regex.
`;

const result1 = text.match(/[Rr]eg[Ee]x/g);
console.log(result1);
