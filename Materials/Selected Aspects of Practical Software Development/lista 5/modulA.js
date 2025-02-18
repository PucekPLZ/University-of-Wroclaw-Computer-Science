const modulB = require('./modulB')

console.log('Moduł A został załadowany.')

exports.funkcjaA = () => {
  console.log('Funkcja z modułu A.')
  modulB.funkcjaB()
}