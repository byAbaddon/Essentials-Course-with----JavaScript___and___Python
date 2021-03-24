function oddEvenSum(arg) {
    let loop = arg.shift()
    let evenSum = 0
    let oddSum = 0

    for (let i = 0; i < loop; i++) {
        let currentNum = +arg.shift()

        if (i & 1) {
            oddSum += currentNum
        } else {
            evenSum += currentNum
        }
    }

    return evenSum == oddSum ? `Yes\nSum = ${evenSum}` : `No\nDiff = ${Math.abs(evenSum - oddSum)}`
}

// console.log(oddEvenSum([4, 10, 50, 60, 20]))