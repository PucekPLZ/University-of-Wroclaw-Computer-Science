function recFib(n) {
    if (n <= 1) {
        return n
    } else {
        return recFib(n-2) + recFib(n-1)
    }
}

function memoFib(fn) {

    var cache = {}

    return function(n) {

        if (n in cache) {
            console.log("acc")
            return cache[n]
        } else {
            var result = fn(n)
            cache[n] = result;
            return result
        }
    }
}

console.time()
console.log(recFib(20))
console.timeEnd()


recFib = memoFib(recFib)
console.time()
console.log(recFib(20))
console.timeEnd()
console.log(recFib(19))