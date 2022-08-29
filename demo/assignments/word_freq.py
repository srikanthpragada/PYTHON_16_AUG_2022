# Take a string and display how many times each word is occurring

text = "Do you like Python or do you like Java more than you like Python"
words = text.split(" ")
for word in sorted(set(words)):
    print(word, words.count(word))

