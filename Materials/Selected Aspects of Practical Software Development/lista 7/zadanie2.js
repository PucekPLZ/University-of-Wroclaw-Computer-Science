const https = require('https')
const fs = require('fs')

const pfxFilePath = 'localhost.pfx'
const pfxPassphrase = 'lucjan'

const options = {
    pfx: fs.readFileSync(pfxFilePath),
    passphrase: pfxPassphrase
}

https.createServer(options, (req, res) => {
    res.end('Hello, world!\n')
    }).listen(3000, () => {console.log('started')})

// https://localhost:3000/