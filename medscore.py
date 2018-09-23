from vaderSentiment import sentiment as vaderSentiment 
import json
jsonFile = open('user_report.json', 'r')
sentences = json.load(jsonFile)
for p in sentences['symptom']:
    sentiment = vaderSentiment(p)
    print(sentiment)
