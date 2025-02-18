function forEach(a, f) {
    for (let i = 0; i < a.length; i ++) {
        f(a[i])
    }
}

function filter(a, f) {
    new_list = []

    for (let i = 0; i < a.length; i ++) {
        if (f(a[i])) {
            new_list.push(a[i])
        }
    }
    return new_list
}

function map(a, f) {
    for (let i = 0; i < a.length; i ++) {
        a[i] = f(a[i])
    }
    return a
}

var a = [1,2,3,4]

forEach(a, _ => {console.log(_)})
console.log("")
console.log(filter(a, _ => _ < 3))
console.log("")
console.log(map(a, _ => _ * 2))