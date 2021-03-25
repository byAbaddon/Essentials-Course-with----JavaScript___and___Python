function evenAndOddSubtraction(arg) {
    let evenNum = arg.filter(el => !(el & 1))
    let oodNum = arg.filter(el => el & 1)

    if (evenNum.length > 0)
        evenNum = evenNum.reduce((a, b) => a + b)

    if (oodNum.length > 0) 
        oodNum = oodNum.reduce((a, b) => a + b)
    
    return evenNum - oodNum
}

// console.log(evenAndOddSubtraction([1, 2, 3, 4, 5, 6]))
// console.log(evenAndOddSubtraction([3, 5, 7, 9]))