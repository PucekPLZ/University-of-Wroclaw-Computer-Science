const modulA = require('./modulA')

console.log('Moduł B został załadowany.')

exports.funkcjaB = () => {
    console.log('Funkcja z modułu B.')
    modulA.funkcjaA()
}