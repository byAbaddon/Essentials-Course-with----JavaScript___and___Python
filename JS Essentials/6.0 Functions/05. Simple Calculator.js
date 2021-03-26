function simpleCalculator(nOne, nTwo, operator) {
    const operatorObj = {'multiply': '*', 'divide': '/', 'add' : '+', 'subtract': '-' }
    return eval(nOne + operatorObj[operator] + nTwo)
}

// console.log(simpleCalculator(5, 5, 'multiply'))
// console.log(simpleCalculator(40, 8, 'divide'))