let input = require('fs').readFileSync('/dev/stdin').toString().split(' ')

let a = parseFloat(input[0])
let b = parseFloat(input[1])

console.log(a/b)