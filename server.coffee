express = require 'express'
app = express()

app.get '/', (req, res) ->
    res.sendFile index.html
    return

app.listen 8080, () ->
    console.log 'up on 8080'