function fibIter() {
    let a = 1
    let b = 1

    return {
        next: function () {
            let current = a
            a = b
            b = current + b
            return { 
                value: current, 
                done: false
            }
        }
    }
}

function* fibGen() {
    let a = 1
    let b = 1

    while (true) {
        yield a
        let current = a
        a = b
        b = current + b
    }
}

var _it = fibIter()
for (var _result; _result = _it.next(), !_result.done;) {
    console.log(_result.value)
}

var _it = fibGen()
for (var _result; _result = _it.next(), !_result.done;) {
    console.log(_result.value)
}

// for-of po generatorze, po iteratorze nie dziala 
for (var i of fibGen()) {
    console.log(i)
}