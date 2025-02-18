var p = {
    name: 'jan',

    say: function() {
        return this.name;
    }
}

var q = {
    surname: 'kowalski'
}

Object.setPrototypeOf(p, q)
console.log(p.name)
console.log(p.surname)

console.log(p.hasOwnProperty('name'))

function OwnProp(obj,property){
    return obj.hasOwnProperty(property)
}

p.foo = "foo"

console.log(OwnProp(p, 'surname'))
console.log(Object.getOwnPropertyNames(p))

function printProperties(obj) {
    console.log(Object.getOwnPropertyNames(obj))
  
    const pro = Object.getPrototypeOf(obj)

    if (pro !== null) {
      printProperties(pro)
    }
}
printProperties(p)