from text_cleaner import clean_text
from sentiment_analyzer import get_sentiment
from visualization import generate_wordcloud, plot_sentiment

def main():
    print("=== Text Sentiment Analyzer ===")
    print("1. Enter text manually")
    print("2. Read from file (data/input_text.txt)")
    choice = input("Choose an option (1/2): ")

    if choice == "1":
        text = input("Enter your text: ")
    elif choice == "2":
        try:
            with open("../data/input_text.txt", "r") as file:
                text = file.read()
        except FileNotFoundError:
            print("Error: File not found!")
            return
    else:
        print("Invalid choice!")
        return

    cleaned_text = clean_text(text)
    sentiment = get_sentiment(cleaned_text)
    
    print("\n=== Results ===")
    print(f"Sentiment: {sentiment}")
    
    generate_wordcloud(cleaned_text)
    plot_sentiment([sentiment])

if __name__ == "__main__":
    main()