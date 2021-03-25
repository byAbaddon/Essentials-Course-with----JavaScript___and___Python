function condenseArrayToNumber(arg) {

   if (arg.length == 1) 
       return +arg[0]
   
    let condensed = 0
    let num = []

    while (arg.length != 1) {
        condensed = +arg.shift() + +arg[0]
        num.push(condensed)
        if (arg.length == 1 && num.length > 1) {
            arg = [...num]
            num = []
        } 
    }

    return num.reduce((a, b) => a + b)
}

// console.log(condenseArrayToNumber([2, 10, 3]))
// console.log( condenseArrayToNumber([5,0,4,1,2]))
// console.log( condenseArrayToNumber([1]))