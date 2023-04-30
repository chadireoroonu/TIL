let input = require('fs').readFileSync('/dev/stdin').toString()

let star = ''

for (let i = 0; i < input; i++) {
    for (let j = input - i; j > 0; j--) {
        star += '*'
    }
    console.log(star)
    star = ''
}