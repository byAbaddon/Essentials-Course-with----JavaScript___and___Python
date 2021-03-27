function convertToObject(arg) {
    let info = JSON.parse(arg)

    for (const key of Object.keys(info)) {
        console.log(key + ': ' + info[key])
    }
}

// convertToObject('{"name": "George", "age": 40, "town": "Sofia"}')