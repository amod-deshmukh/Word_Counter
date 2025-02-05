import re

def count_words(text):
    # Use regex to find only words (alphanumeric sequences)
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def main():
    # Prompt user input
    user_input = input("Enter a sentence or paragraph: ").strip()
    
    # Error handling for empty input
    if not user_input:
        print("Error: No input provided. Please enter some text.")
        return

    # Count words and display result
    word_count = count_words(user_input)
    print(f"Word Count: {word_count}")

if __name__ == "__main__":
    main()
