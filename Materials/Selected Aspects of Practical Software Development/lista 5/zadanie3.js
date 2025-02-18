const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const wylosowanaLiczba = Math.floor(Math.random() * 101)

function gra() {
    rl.question('zgadnij liczbę od 0 do 100: ', (odpowiedz) => {
        const podanaLiczba = parseInt(odpowiedz)

        if (isNaN(podanaLiczba)) {
            console.log('podana wartość nie jest liczbą')
        } else if (podanaLiczba == wylosowanaLiczba) {
            console.log('to jest właśnie ta liczba')
            rl.close()
        } else if (podanaLiczba < wylosowanaLiczba) {
            console.log('moja liczba jest większa')
            gra()
        } else {
            console.log('moja liczba jest mniejsza')
            gra()
        }
    })
}

gra()