function wrongResult(...arg) {
    let counter = 0

    for (const el of arg) {
        if (el < 0) {
            counter++
        } else if (el == 0) {
            return 'Positive'
        }
    }

    return counter === 1 || counter === 3 ? 'Negative' : 'Positive'
}

// console.log(wrongResult(5, 12, -15))
//console.log(wrongResult(-6, -12, 14))
// console.log(wrongResult(-1, 0, 1))