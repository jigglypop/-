var fs = require("fs");
// var input = fs.readFileSync("/dev/stdin", "utf8").split("\n");
var input = fs.readFileSync("./2504.txt", "utf8").split("\r\n");
var blackets = input[0];
var result = 0

const check = () =>{
    let S = []
    const pair = {'(':')', '[':']'}

    for (let blacket of blackets){
        if (!S.length){
            S.push(blacket)
        }
        else if (pair[blacket] === undefined){
            if (pair[S[S.length - 1]] === blacket){
                S.pop()
            } else {
                S.push(blacket)
            }
        } else {
            S.push(blacket)
        }
    }
    return S.length ? false : true
}


const calc = () =>{
    let S = []
    const pair = {'(':')', '[':']'}
    const cost = {')' : 2, ']' : 3}
    for (let blacket of blackets){
        console.log(S)
        if (!S.length){
            S.push(blacket)
        }
        else if (pair[blacket] === undefined){
            let last = S[S.length - 1]
            if (pair[last] === blacket){
                S.pop()
                S.push(cost[blacket])
            } else {
                let temp = 0
                for (let i = S.length - 1; i >= 0;i--){
                    temp += S.pop()
                }
                S.push(cost[pair[last]]* temp)
            }
        }
    }
    console.log(S)
    return S
}
console.log(blackets)
calc()
console.log()