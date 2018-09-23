express = require 'express'
app = express()

app.get '/', (req, res) ->
    res.sendFile __dirname+'/index.html'
    return 

app.listen 8080, () ->
    console.log 'up on 8080'