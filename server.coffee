express = require 'express'
mongoose = require 'mongoose'
mongoose.connect 'mongodb://medefine:medefine0@ds111913.mlab.com:11913/medefine'
child = require 'child_process'
app = express()

patientSchema = new mongoose.Schema {
    name: String,
    password: Number,
    symptomScores: Array,
    bias: Number,
    primaryDocEmail: String,
    email: String
}
doctorSchema = new mongoose.Schema {
    name: String,
    password: Number,
    department: String,
    email: String
}
adminSchema = new mongoose.Schema {
    name: String,
    password: Number,
    email: String
}
appointmentSchema = new mongoose.Schema {
    patientEmail: String,
    doctorEmail: String,
    time: Date
}

patient = mongoose.model 'patient', patientSchema
doctor = mongoose.model 'doctor', doctorSchema
admin = mongoose.model 'admin', adminSchema
appointment = mongoose.model 'appointment', appointmentSchema

app.use express.static 'www'
app.use express.json()
app.use express.urlencoded()

app.get '/', (req, res) ->
    res.sendFile __dirname+'/www/index.html'
    return

app.post '/symptoms', (req, res) ->
    uname = req.body.uname
    symptoms = req.body.symptoms
    console.log uname
    console.log symptoms
    patient.findOne {email: uname}, (err, thisParticularPatient) ->
        console.log thisParticularPatient
        if thisParticularPatient == null
            return
        newSymptoms = thisParticularPatient.symptomScores
        scoreps = child.spawn '/usr/bin/python3', ['medscore.py', symptoms]
        scoreps.stdout.on 'data', (data) ->
            newSymptoms.push Number(data)
            biasps = child.spawn '/usr/bin/python3', ['medscore.py'].concat newSymptoms
            biasps.stdout.on 'data', (data2) ->
                thisParticularPatient.set {symptomScores: newSymptoms}
                thisParticularPatient.set {bias: Number(data2)}
                console.log thisParticularPatient
                return
            return
        return    
    res.sendStatus 200
    return

app.listen 8080, () ->
    console.log 'up on 8080'
    