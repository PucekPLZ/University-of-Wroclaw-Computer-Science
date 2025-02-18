function isDivisible(number) {
    let numberString = number.toString()
    let numberLength = numberString.length
    let numberSum = 0

    for (let i = 0; i < numberLength; i++) {
        let digit = parseInt(numberString[i])
        if (number % digit != 0) {
            return false
        }

        numberSum += digit
    }

    if (number % numberSum != 0) {
        return false       
    }

    return true
}

function set(a, b) {
    let numbers = []

    for (let i = a; i <= b; i++) {
        if (isDivisible(i)) {
            numbers.push(i)
        }
    }

    return numbers
}

console.log(100 / 0)

console.log(set(1, 100000))