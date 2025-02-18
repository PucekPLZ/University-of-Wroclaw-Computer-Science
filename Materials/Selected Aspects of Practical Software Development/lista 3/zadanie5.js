function createGenerator(n) {
    return function() {
        var state = 0
        return {
            next: function () {
                return {
                    value: state,
                    done: state++ >= n
                }
            }
        }
    }
}

var foo1 = {
    [Symbol.iterator]: createGenerator(10)
}

var foo2 = {
    [Symbol.iterator]: createGenerator(20)
}

for (var i of foo1) {
    console.log(i)
}
console.log("")
for (var i of foo2) {
    console.log(i)
}