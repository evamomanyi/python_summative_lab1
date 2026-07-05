import re
from collections import Counter


# -----------------------------
# Function 1: Count Specific Word
# -----------------------------
def count_specific_word(text, search_word):
    """
    Counts the number of occurrences of a specific word.
    Returns an integer.
    """

    if not text:
        return 0

    # Extract words and ignore punctuation
    words = re.findall(r"\b\w+\b", text.lower())

    return words.count(search_word.lower())


# -----------------------------
# Function 2: Identify Most Common Word
# -----------------------------
def identify_most_common_word(text):
    """
    Returns the most common word.
    Returns None for an empty string.
    """

    if not text.strip():
        return None

    words = re.findall(r"\b\w+\b", text.lower())

    if len(words) == 0:
        return None

    word_counts = Counter(words)

    return word_counts.most_common(1)[0][0]


# -----------------------------
# Function 3: Calculate Average Word Length
# -----------------------------
def calculate_average_word_length(text):
    """
    Calculates the average word length.
    Returns a float.
    """

    if not text.strip():
        return 0

    words = re.findall(r"\b\w+\b", text)

    if len(words) == 0:
        return 0

    total_letters = sum(len(word) for word in words)

    return total_letters / len(words)


# -----------------------------
# Function 4: Count Paragraphs
# -----------------------------
def count_paragraphs(text):
    """
    Counts paragraphs separated by blank lines.
    Returns an integer.
    """

    if not text.strip():
        return 1

    paragraphs = [p for p in text.split("\n\n") if p.strip()]

    return len(paragraphs)


# -----------------------------
# Function 5: Count Sentences
# -----------------------------
def count_sentences(text):
    """
    Counts sentences ending with . ! or ?
    Returns an integer.
    """

    if not text.strip():
        return 1

    sentences = re.findall(r"[.!?]+", text)

    return len(sentences)


# ====================================================
# Main Program
# ====================================================

def main():

    filename = "news_article.txt"

    try:
        with open(filename, "r", encoding="utf-8") as file:
            article = file.read()

    except FileNotFoundError:
        print("Error: news_article.txt was not found.")
        return

    print("====== NEWS ARTICLE ANALYSIS ======\n")

    # Ask the user for a word
    search_word = input("Enter a word to search for: ")

    count = count_specific_word(article, search_word)

    print(f"\nThe word '{search_word}' appears {count} time(s).")

    common_word = identify_most_common_word(article)

    print(f"The most common word is: {common_word}")

    average_length = calculate_average_word_length(article)

    print(f"Average word length: {average_length:.2f}")

    paragraphs = count_paragraphs(article)

    print(f"Number of paragraphs: {paragraphs}")

    sentences = count_sentences(article)

    print(f"Number of sentences: {sentences}")


# Run program
if __name__ == "__main__":
    main()