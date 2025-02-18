const express = require('express')
const app = express()
const multer = require('multer')
const upload = multer({dest: './zadanie1/uploads/'})

app.use(express.static('public'))
app.set('view engine', 'ejs')
app.use(express.urlencoded({extended: true}))
app.set('views', './zadanie1/views')

const port = 3000;

app.get('/', (req, res) => {
    res.render('main.ejs')
})

app.post('/', upload.single('file1'), (req, res) => {
    req.file ? res.send('File uploaded') : res.send('No file uploaded')
})

app.listen(port, () => console.log(`Server started at port http://localhost:${port}`))