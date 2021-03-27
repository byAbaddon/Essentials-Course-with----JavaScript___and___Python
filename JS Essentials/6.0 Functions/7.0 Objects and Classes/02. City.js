function city(...arg) {
    let [name, area, population , country, postCode] = [...arg]
    let infoObj = {name, area, population, country, postCode}
    
    for (const [key,val] of Object.entries(infoObj)) {
        console.log(key + ' -> ' + val);
    } 
}

// city("Sofia"," 492", "1238438", "Bulgaria", "1000")