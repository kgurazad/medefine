from vaderSentiment import sentiment as vaderSentiment 
import json
jsonFile = open('your_filename.json', 'r')
sentences = json.load(jsonFile)
for p in sentences['symptom']:
    sentiment = vaderSentiment(p)
    with open('scores.json', 'r' as f):
        s = json.load(f)
        s.append(sentiment)
        json.dump(s,f)
