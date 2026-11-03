def largest_word(sentence):
    words = sentence.split()

    if not words:
        return ""

    return max(words, key=len)


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    result = largest_word(sentence)
    print("Largest word:", result)