from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig("data/outputs/wordcloud.png")  
    plt.show()

def plot_sentiment(sentiments):
    counts = {
        "Positive": sentiments.count("Positive"),
        "Negative": sentiments.count("Negative"),
        "Neutral": sentiments.count("Neutral")
    }
    plt.bar(counts.keys(), counts.values(), color=["green", "red", "blue"])
    plt.title("Sentiment Analysis")
    plt.savefig("data/outputs/sentiment_plot.png")  # Save to file
    plt.show()