function isPrime(number) {
    let i = 2

    while (i < number) {
        if (number % i == 0) {
            return false
        }

        i++
    }

    return true
}

function set(a, b) {
    let primeNumbers = []

    for (let i = a; i <= b; i++) {
        if (isPrime(i)){
            primeNumbers.push(i)
        }
    }

    return primeNumbers
}

console.log(set(2, 100000))