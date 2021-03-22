function fishTank(arg){
    let [long, width,  hight, percent] = [...arg]
    let size = long * width * hight * 0.001
    let pr = percent * 0.01
    return (size * (1 - pr)).toFixed(3)     
 }
 
// console.log(fishTank([85, 75, 47, 17]))