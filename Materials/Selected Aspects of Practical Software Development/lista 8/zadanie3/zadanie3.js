const express = require('express')
const app = express()
const port = 3000

app.get('/' , (req, res) => {
    res.setHeader('Content-Disposition', 'attachment; filename=file.txt')
    res.send('Hello World!')
})

app.listen(port, () => console.log(`Server started at port http://localhost:${port}`))