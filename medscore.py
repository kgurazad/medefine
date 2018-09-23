from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sys
sys.stderr.write("started medscore!\n")
analyser = SentimentIntensityAnalyzer()
s = sys.argv[1]
snt = analyser.polarity_scores(s)
print(snt)
sys.stderr.write(String(snt))
sys.stderr.write("finished medscore!\n")