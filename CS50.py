import convertapi
import os


def main():
    pdfFinder()
    filename = input("Enter the file name(without the '.pdf'): ")
    convertToText(filename)
    
    file_path = "C:/Users/harun/Desktop/CS50 PROJE/CS50-Project/PDF/" + filename + ".txt"

    # Check if file exists
    if not os.path.exists(file_path):
        print("Warning: File does not exist.")
        return 1
    else:
        with open(file_path, 'r', encoding="utf8") as file:
            file_content = file.read()

        file_content_without_newlines = file_content.replace('\n', '')

        with open(file_path, 'w', encoding="utf8") as file:
            file.write(file_content_without_newlines)


    with open(file_path, "r",  encoding="utf8") as f:
        contents = f.read()
        
    text = contents
    letter_count = letter(text)
    sentence_count = sentence(text)
    word_count = word(text)
    index = coleman(letter_count, sentence_count, word_count)

    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


def sentence(text):
    sentence_count = 0
    for i in text:
        if i in [".", "!", "?"]:
            sentence_count += 1
    return sentence_count


def word(text):
    words = text.split()
    return len(words)


def letter(text):
    letter_count = 0
    for w in text:
        if w.isalpha():
            letter_count += 1
    return letter_count


def coleman(letter_count, sentence_count, word_count):
    L = letter_count / word_count * 100
    S = sentence_count / word_count * 100

    index = 0.0588 * L - 0.296 * S - 15.8
    index = round(index)
    return index

def convertToText(filename):
    convertapi.api_secret = 'o7bk50o9CVHqCwX7'
    while True:
        file_path = 'C:/Users/harun/Desktop/CS50 PROJE/CS50-Project/' + filename + ".pdf"
        if not os.path.exists(file_path):
            print("Warning: File does not exist.")
            filename = input("Enter the file name(without the '.pdf'): ")
        else:
            break
    new_file_path = 'C:/Users/harun/Desktop/CS50 PROJE/CS50-Project/PDF/' + filename + ".txt"
    if os.path.exists(new_file_path):
        return 1
    convertapi.convert('txt', {
        'File': file_path
    }, from_format='pdf').save_files('C:/Users/harun/Desktop/CS50 PROJE/CS50-Project/PDF')

def pdfFinder():
    pdf_files = []
    for file in os.listdir('C:/Users/harun/Desktop/CS50 PROJE/CS50-Project'):
        if file.endswith(".pdf"):
            pdf_files.append(file)

    if len(pdf_files) == 0:
        print("No PDF files found.")
    else:
        print("All PDF files listed here:")
        for file in pdf_files:
            print(file)
main()
