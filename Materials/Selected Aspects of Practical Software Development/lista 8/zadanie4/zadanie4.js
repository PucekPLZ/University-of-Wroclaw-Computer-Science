const express = require('express')
const app = express()
const cookieParser = require('cookie-parser')

app.set('view engine', 'ejs')
app.set('views', './zadanie4/views')
app.use(cookieParser())
app.use(express.urlencoded({extended: true}))

const port = 3000

app.get('/', (req, res) => {
    var cookieValue = new Date().getTime().toString()
    res.cookie('cookie', cookieValue, { maxAge: 1000 * 60 * 60 * 24 * 365 })
    res.render('index.ejs', { cookie: cookieValue })
})

app.post('/', (req, res) => {
    res.clearCookie('cookie')
    res.redirect('/deleted')
})

app.get('/deleted', (req, res) => {
    res.render('deleted.ejs', { message: "Cookie was successfully deleted." })
})

app.listen(port, () => console.log(`Server started at port http://localhost:${port}`))