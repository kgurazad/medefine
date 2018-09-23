express = require 'express'
app = express()

app.use express.static 'www'
app.use express.json()
app.use express.urlencoded()

app.get '/', (req, res) ->
    res.sendFile __dirname+'/www/index.html'
    return

app.post '/symptoms', (req, res) ->
    console.log req.body
    console.log 'POST'
    res.sendStatus 200
    return

app.listen 8080, () ->
    console.log 'up on 8080'
    