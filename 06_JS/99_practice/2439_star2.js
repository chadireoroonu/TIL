let input = require('fs').readFileSync('/dev/stdin').toString()

let star = ''
let space = ''

for (let i = 1; i <= input; i++) {
    star += '*'
    for (let j = 0; j < input - i; j++) {
        space += ' '
    }
    console.log(space + star)
    space = ''
}