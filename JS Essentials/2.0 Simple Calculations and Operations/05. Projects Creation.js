function projectsCreation(arg) {
    let [name, projects] = [...arg]
    return `The architect ${name} will need ${projects * 3} hours to complete ${projects} project/s.`
}

//console.log(projectsCreation(['George', 4]))