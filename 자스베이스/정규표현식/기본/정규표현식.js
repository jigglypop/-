text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다";

const phone1 = /\d\d\d-\d\d\d-\d\d\d\d/g.exec(text);
const phone2 = /\d{3}-\d{3}-\d{4}/g.exec(text);

console.log(phone1);
console.log(phone2);
