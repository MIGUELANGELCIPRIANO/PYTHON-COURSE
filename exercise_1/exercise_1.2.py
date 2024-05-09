sentence = input("Enter a sentence: ")
words = sentence.split(" ")
word_count = len(words)
print(
    f"You enter {word_count} words and it would take you {word_count/2} seconds to pronounce them"
)
