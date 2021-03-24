function numberSequence(arg) {
    rm = arg.shift()
    return`Max number: ${Math.max(...arg)}\nMin number: ${Math.min(...arg)}` 
}

// console.log(numberSequence([5,10,20,304,0,50]))