# PDF Text Analyzer
This Python script is designed to analyze text content extracted from PDF files and determine the readability score based on the Coleman-Liau index.

This script is designed to perform two main functions:
* **PDF to Text Conversion:**
    It converts PDF files located in the specified directory into text files using the '*convertapi*' library.
* **Readability Index Calculation:** After converting a PDF to text, this script calculates the readability index of the text content using the Coleman-Liau index formula.

## Requirements
* Python 3.x
* '*convertapi*' Python package (install via pip install convertapi)

## Usage
1. Place your PDF files in the directory: '*C:/Users/harun/Desktop/CS50 PROJE/CS50-Project/*'
1. Run the main() function from the script '*pdf_text_analyzer.py*'
1. The program will prompt you to enter the filename (without the '.pdf') you want to analyze.
1. Script will convert the PDF to text and analyze the text's readability using the Coleman-Liau index.
1. The calculated readability index will be displayed in the console.

## File Structure
### Included Libraries
1. convertapi
1. os

### Functionality
* **pdfFinder():** Lists all the PDF files present in the specified directory.
* **convertToText(filename):** Converts the specified PDF file to text using ConvertAPI and saves it as a .txt file.
* **main():** Controls the main flow of the program, prompts for user input, performs text analysis, and calculates the readability score.
* **letter(text):** Calculates the total number of letters in the provided text.
* **sentence(text):** Counts the number of sentences in the provided text.
* **word(text):** Counts the number of words in the provided text.
* **coleman(letter_count, sentence_count, word_count):** Calculates the Coleman-Liau index based on the counts of letters, sentences, and words.


## Example Usage
```ruby
$ python script.py
Enter the file name(without the '.pdf'): example_file
Grade 8
```

### Note
* The analyzed text file will be saved in the directory: '*C:/Users/harun/Desktop/CS50 PROJE/CS50-Project/PDF/.*'