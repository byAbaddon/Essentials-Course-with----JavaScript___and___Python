function convertToJSON(...arg) {
    let [name, lastName, hairColor] = [...arg]
    let obj = {name, lastName, hairColor}
    return JSON.stringify(obj)
}

// console.log(convertToJSON('George', 'Jones', 'Brown'))