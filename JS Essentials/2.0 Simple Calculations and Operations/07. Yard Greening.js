function yard(kvM) {
    let price = kvM * 7.61
    let discount = price * 0.18

    return `The final price is: ${(price - discount).toFixed(2)} lv.\nThe discount is: ${discount.toFixed(2)} lv.`
}

// console.log(yard(550))