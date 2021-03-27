function info(...arg) {
    let [fName, lName, age] = [...arg]
    let infoObj = {'firstName': fName, 'lastName' : lName, 'age' : age}
    
    for (const [key,val] of Object.entries(infoObj)) {
        console.log(key + ': ' + val);
    } 
}

// info('Peter', 'Pan', '20')