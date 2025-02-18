function iterFib(n) {
    let fib0 = 0
    let fib1 = 1
    let fib = 0

    let i = 1

    while (i < n) {
        fib = fib0 + fib1
        fib0 = fib1
        fib1 = fib

        i++
    }

    return fib
}

function recFib(n) {
    if (n <= 1) {
        return n
    } else {
        return recFib(n-2) + recFib(n-1)
    }
}

console.time()
console.log(iterFib(35))
console.timeEnd()

console.time()
console.log(recFib(35))
console.timeEnd()