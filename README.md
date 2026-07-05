# News Article Text Analysis

## Project Overview

This project is a Python application that analyzes a news article stored in a text file. The program performs several Natural Language Processing (NLP) text analysis tasks, including counting the occurrences of a specific word, identifying the most common word, calculating the average word length, counting paragraphs, and counting sentences.

The project demonstrates the use of Python functions, file handling, regular expressions, dictionaries, and basic text processing techniques.

---

## Objectives

The program performs the following tasks:

* Count the number of times a specific word appears in a news article.
* Identify the most frequently used word.
* Calculate the average length of words.
* Count the number of paragraphs.
* Count the number of sentences.

---

## Project Structure

```
PythonAssessment/
│
├── pythonAssessment.py      # Main Python program
├── news_article.txt         # News article to analyze
└── README.md                # Project documentation
```

---

## Requirements

* Python 3.8 or later
* Visual Studio Code (recommended) or another Python IDE

No third-party libraries are required. The program only uses Python's standard library.

---

## Python Modules Used

The program imports the following built-in modules:

```python
import re
from collections import Counter
```

* **re** is used for pattern matching and removing punctuation.
* **Counter** is used to determine the most common word efficiently.

---

## Program Features

### 1. Count Specific Word

**Function**

```python
count_specific_word(text, search_word)
```

Counts how many times a user-specified word appears in the article.

**Parameters**

* `text` – the news article
* `search_word` – the word to search for

**Returns**

An integer representing the number of occurrences.

**Edge Case**

Returns `0` if the word does not exist or the text is empty.

---

### 2. Identify the Most Common Word

**Function**

```python
identify_most_common_word(text)
```

Determines which word appears most frequently in the article.

**Returns**

The most common word as a string.

**Edge Case**

Returns `None` if the text is empty.

---

### 3. Calculate Average Word Length

**Function**

```python
calculate_average_word_length(text)
```

Calculates the average number of letters per word.

Punctuation is ignored during the calculation.

**Returns**

A floating-point number.

**Edge Case**

Returns `0` for an empty string.

---

### 4. Count Paragraphs

**Function**

```python
count_paragraphs(text)
```

Counts paragraphs by identifying blank lines between blocks of text.

**Returns**

The number of paragraphs.

**Edge Case**

Returns `1` for an empty string.

---

### 5. Count Sentences

**Function**

```python
count_sentences(text)
```

Counts sentences based on sentence-ending punctuation:

* Period (.)
* Exclamation mark (!)
* Question mark (?)

**Returns**

The number of sentences.

**Edge Case**

Returns `1` for an empty string.

---

## How to Run the Program

1. Place the news article inside a file named:

```
news_article.txt
```

2. Ensure the file is in the same directory as:

```
pythonAssessment.py
```

3. Open a terminal.

4. Navigate to the project folder.

5. Run the program:

```bash
python pythonAssessment.py
```

or

```bash
python3 pythonAssessment.py
```

depending on your Python installation.

---

## Example Output

```
====== NEWS ARTICLE ANALYSIS ======

Enter a word to search for: Pie

The word 'Pie' appears 21 time(s).
The most common word is: the
Average word length: 5.22
Number of paragraphs: 19
Number of sentences: 48
```

---

## Testing

The following tests were performed:

| Test Case                            | Expected Result                           |
| ------------------------------------ | ----------------------------------------- |
| Search for an existing word          | Correct occurrence count                  |
| Search for a word not in the article | Returns 0                                 |
| Empty text file                      | Edge-case values returned                 |
| One paragraph                        | Paragraph count = 1                       |
| Multiple paragraphs                  | Correct paragraph count                   |
| Text with punctuation                | Accurate sentence count                   |
| Text without punctuation             | Sentence count based on punctuation rules |

---

## Error Handling

The program checks whether the input file exists before attempting to read it.

If the file cannot be found, the program displays:

```
Error: news_article.txt was not found.
```

instead of crashing.

---

## Coding Best Practices

This project follows Python best practices by:

* Using descriptive function names.
* Keeping each function focused on a single task.
* Including function documentation (docstrings).
* Handling edge cases.
* Using meaningful variable names.
* Separating logic into reusable functions.
* Using Python's standard library instead of external packages.

---

## Possible Improvements

Future enhancements could include:

* Ignoring common stop words (such as *the*, *is*, and *and*) when identifying the most common word.
* Displaying the top 10 most common words.
* Exporting analysis results to a CSV or text file.
* Adding a graphical user interface (GUI).
* Supporting additional file formats such as PDF and Microsoft Word documents.
* Visualizing word frequencies with charts.

---

