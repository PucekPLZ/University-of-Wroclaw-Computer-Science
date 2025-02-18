const express = require('express')
const app = express()

app.use(express.static('public'))
app.set('view engine', 'ejs')
app.use(express.urlencoded({extended: true}))

app.get('/', (req, res) => {
    res.render('form.ejs', errors = {})
})

app.post('/', (req, res) => {
    const {name, surname, subject, tasks} = req.body

    if(!name.length || !surname.length || !subject.length) {
        res.render('form.ejs', {errors: {error: 'Fill in all fields'}})
        console.log(errors)
        return
    }

    const taskArr = Array.isArray(tasks) ? tasks.map(Number) : [Number(tasks)]
    console.log(taskArr)
    
    res.redirect(`/print?name=${name}&surname=${surname}&subject=${subject}&taskArr=${JSON.stringify(taskArr)}`)
})

app.get('/print', (req, res) => {
    var {name, surname, subject, taskArr} = req.query
    taskArr = JSON.parse(taskArr)
    console.log(taskArr)

    if(!name.length || !surname.length || !subject.length) {
        res.redirect('/')
        return
    }

    res.render('print.ejs', {name, surname, subject, taskArr})
})

const port = 3000;
app.listen(port, () => console.log(`Server started at port http://localhost:${port}`))