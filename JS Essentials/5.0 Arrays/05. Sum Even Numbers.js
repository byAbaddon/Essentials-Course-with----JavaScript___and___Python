function sumEvenNumbers(arg) {
    let result = arg.map(Number).filter(el => !(el & 1))
    return result == 0 ? 0 : result.reduce((a, b) => a + b)
}

// console.log(sumEvenNumbers(['1', '2', '3', '4', '5', '6']))
// console.log(sumEvenNumbers(['3','5','7','9']))