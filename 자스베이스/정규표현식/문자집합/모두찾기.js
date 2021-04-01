const text = `
    sales1.xls
    orders3.xls
    sales2.xls
    apac1.xls
    europe2.xls
    sam.xls
    na1.xls
    na2.xls
    sa1.xls
    ca1.xls
`;

const result1 = text.match(/.a.\.xls/g);
const result2 = text.match(/[ns]a.\.xls/g);
const result3 = text.match(/[ns]a[0-9]\.xls/g);

console.log(result1);
console.log(result2);
console.log(result3);
