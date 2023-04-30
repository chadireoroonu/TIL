let input = require('fs').readFileSync('/dev/stdin').toString()

let star = ''
let space = ''

for (let i = 0; i < input; i++) {
    for (let j = 0; j < i; j++) {
        space += ' '
    }
    for (let k = input - i; k > 0; k--) {
        star += '*'
    }
    console.log(space + star)
    star = ''
    space = ''
}