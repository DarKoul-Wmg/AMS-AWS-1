const express = require('express')
const fs = require('fs/promises')
const url = require('url')
const post = require('./post.js')
const ejs = require('ejs')

const app = express()
const port = 3000

// Iniciar el sistema de plantilles
app.set('view engine', 'ejs')

// Publicar els arxius de la carpeta 'public'
app.use(express.static('public'))

// Activar el servidor
app.listen(port, appListen)
function appListen () {
  console.log(`Example app listening on: http://localhost:${port}`)
}

// Definir URLs i el què es mostra

app.get('/ejs', getEjsIndex)
async function getEjsIndex (req, res) {
  let dades = {}
  res.render('sites/index', dades)
}