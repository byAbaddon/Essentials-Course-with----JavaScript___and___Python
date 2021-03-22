function concatenateData(arg) {
    let [firstName, lastName, age, town] = [...arg]
    return `You are ${firstName} ${lastName}, a ${age}-years old person from ${town}.`

}

// console.log(concatenateData(['Mara', 'Otvarachkata', 27, 'Pichkovci']))