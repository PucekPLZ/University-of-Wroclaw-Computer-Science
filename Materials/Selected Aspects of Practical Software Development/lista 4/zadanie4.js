var n = 1
// liczba ma prototyp? nie
console.log(Object.getPrototypeOf(n))
console.log(typeof Object.getPrototypeOf(n))
// można jej dopisać pole/funkcję? undefined
n.foo = 'foo'
console.log(n.foo)