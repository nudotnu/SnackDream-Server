const nugu = require('./config.json')
const express = require('express')
const bodyParser = require('body-parser')
const app = express()

app.use(express.json())
app.use(bodyParser.json())

app.use('/snack', (req, res) => {
    const cal = nugu.action.parameters['calorie'].value
    console.log(cal)
    let output = nugu.output

    switch(cal){
        case "초콜릿": 
        console.log(cal+"은 100g당 약 550칼로리 입니다."); 
        output = {
            "prompt" : cal+"은 100g당 약 550칼로리 입니다."
        }
        break;

        case "사탕" : 
        console.log(cal+"은 3개당(14g) 52칼로리 입니다."); 
        output = {
            "prompt" : cal+"은 3개당(14g) 52칼로리 입니다."
        }
    }
    nugu.output = output
    console.log(output)
    return res.json(nugu)
})

app.listen(3000, (err, result) => {
    console.log("누구 서버 시작 : ", 3000)
})