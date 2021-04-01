const text = `
    body {
        background-color: #fefbd8;
    } h1 {
        background-color: #0000ff;
    } div {
        background-color: #d0f4e6;
    } span {
        background-color: #f08970;
    }
`;

// 방법 1
// [ '#fefbd8', '#0000ff', '#d0f4e6', '#f08970' ]
console.log(text.match(/#[A-Fa-f0-9]{6}/g));
