function petShop(arg) {
    let [dogs, other] = [...arg.map(Number)]
    return `${(dogs * 2.50 + other * 4.00).toFixed(2)} lv.`
}

// console.log(petShop([5, 4]))