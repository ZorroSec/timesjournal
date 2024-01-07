const express = require('express')
const app = require('./app/app.js')
const marker = require('marker')
const path = require('path')
app.use(express.json())

app.get('/', (req, res)=>{
    const titlePage = 'TimesJournal'
    res.sendFile(__dirname + '/views/index.html', titlePage)
})