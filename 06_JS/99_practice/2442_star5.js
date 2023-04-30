let input = require('fs').readFileSync('/dev/stdin').toString()

let star = ''
let space = ''

for (let i = 1; i <= input; i++) {
    for (let j = 0; j < 2*i-1; j++) {
        star += '*'
    }
    for (let k = input - i - 1; k >= 0; k--) {
        space += ' '
    }
    console.log(space+star)
    star = ''
    space = ''
}