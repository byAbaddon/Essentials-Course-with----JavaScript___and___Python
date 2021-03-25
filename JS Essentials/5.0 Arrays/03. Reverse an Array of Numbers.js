function reverseAnArrayOfNumbers(n, arg) {
    return arg.splice(0, n).reverse().join(' ')
}

// console.log(reverseAnArrayOfNumbers(3, [10, 20, 30, 40, 50]))