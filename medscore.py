from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sys
analyser = SentimentIntensityAnalyzer()
s = sys.argv[1]
snt = analyser.polarity_scores(s)
print(snt)