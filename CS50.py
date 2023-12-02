


def main():
    text = input("Text: ")
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
    word_count = 0
    for i in text:
        if i == " ":
            word_count += 1
    word_count += 1
    return word_count


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


main()
