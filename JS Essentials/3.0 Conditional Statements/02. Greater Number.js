function greaterNumber(arg) {
    arg = [...arg.map(Number)]
    return Math.max(...arg)
}

// console.log(greaterNumber([5, 3]))