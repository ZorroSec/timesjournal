const marker = require('marker')
const express = require('express')
const app = require('./app/app.js')
require('./routes.js')
app.use(express.static(path.join(__dirname, '/public')))

app.listen(3000, (err)=>{
    if(!err){
        console.log({
            message: 'success'
        })
    }
})