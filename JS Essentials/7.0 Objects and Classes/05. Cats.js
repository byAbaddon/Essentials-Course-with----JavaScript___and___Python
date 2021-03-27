function cats(arg) {

    class Cat {
        constructor(name, age) {
            this.name = name
            this.age = age
        }
    
        meow() { 
            return (`${this.name}, age ${this.age} says Meow`)
        }

    }


    for (let i = 0; i < arg.length; i++) {
        let [name, age] = arg[i].split(' ')
        let myCat = new Cat(name,age)
        console.log( myCat.meow(name, age))
       
    }
}

// cats(['Mellow 2', 'Tom 5'])