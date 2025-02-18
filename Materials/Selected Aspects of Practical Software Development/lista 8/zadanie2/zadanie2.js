const express = require('express')
const mainRoute = require('./routes/mainRoute')

const app = express()
const port = 3000

app.set('view engine', 'ejs')
app.set('views', './zadanie2/views')

app.use('/', mainRoute)

app.listen(port, () => console.log(`Server started at port http://localhost:${port}`))