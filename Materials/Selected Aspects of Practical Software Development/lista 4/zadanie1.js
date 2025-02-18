function getLastProto(o) {
    var p = o;
    do {
        o = p;
        p = Object.getPrototypeOf(o);
    } while (p);
    return o;
}

var personProto = {
    say: function() {
        return this.name;
    }
}

var p1 = {
    name: 'jan'
}

Object.setPrototypeOf(p1, personProto)

var p2 = {
    name: 'tomasz'
}

Object.setPrototypeOf(p2, personProto);

// console.log(Object.getPrototypeOf(p2))
console.log(getLastProto(Object.prototype))

console.log(getLastProto(Object.prototype) === getLastProto(p1))
console.log(getLastProto(p1) === getLastProto(personProto))
console.log(getLastProto(p1) === getLastProto(p2))
console.log(getLastProto(p2) === getLastProto(Object.prototype))