function sumNumbers([...arg]) {
    return arg.shift() == 0 ? 0 : arg.reduce((a, b) => +a + +b)
}

// console.log(sumNumbers([2, 10, 20]))
// console.log(sumNumbers([0]))