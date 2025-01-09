from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

def analyze_diary(text):
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(text)
    if scores['compound'] > 0.5:
        return 'positive'
    elif scores['compound'] < -0.5:
        return 'negative'
    else:
        return 'neutral'
