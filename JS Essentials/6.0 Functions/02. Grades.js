function grades(grade) {
    if (grade >= 2.00 && grade <= 2.99 ) return 'Fail'
    if (grade >= 3.00 && grade <= 3.49 ) return 'Poor'
    if (grade >= 3.50 && grade <= 4.49 ) return 'Good'
    if (grade >= 4.50 && grade <= 5.49 ) return 'Very good'
    if (grade >= 5.50 && grade <= 6.00 ) return 'Excellent'
}

// console.log(grades(4.50))