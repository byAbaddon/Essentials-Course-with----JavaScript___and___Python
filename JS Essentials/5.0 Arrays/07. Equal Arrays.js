function equalArrays(arrOne, arrTwo) {
    let sum = 0

    for (let i = 0; i < arrOne.length; i++) {

        if (arrOne[i] === arrTwo[i]) {
            sum += +arrOne[i]
        } else {
            return `Arrays are not identical. Found difference at ${i} index`
        }
    }

    return `Arrays are identical. Sum: ${sum}`
}

// console.log(equalArrays(['10', '20', '30'], ['10', '20', '30']))
// console.log(equalArrays(['1', '2', '3', '4', '5'], ['1', '2', '4', '4', '5']))