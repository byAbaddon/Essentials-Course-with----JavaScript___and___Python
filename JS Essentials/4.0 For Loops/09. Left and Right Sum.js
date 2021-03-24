function leftAndRightSum(arg) {
    let loop = arg.shift()
    let leftSum = arg.splice(0, loop).reduce((a, b) => +a + +b)
    let rightSum = arg.reduce((a, b) => +a + +b)

    return leftSum == rightSum ? `Yes, sum = ${leftSum}` : `No, diff = ${Math.abs(leftSum - rightSum)}`
}

// console.log(leftAndRightSum([2, 10, 90, 60, 40]))