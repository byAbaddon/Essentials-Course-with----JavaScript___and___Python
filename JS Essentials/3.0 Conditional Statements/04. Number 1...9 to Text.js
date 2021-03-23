function numberToText(n) {
    let numList = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return numList.includes(numList[n]) ? numList[n] : ' number too big'
}

// console.log(numberToText(5))