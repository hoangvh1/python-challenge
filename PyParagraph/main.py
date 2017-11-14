x = open("paragraph_1.txt","r")
for words in x:
    wordscount = words.split(" ")
    num_words = len(wordscount)+1
    print("Paragraph Analysis")
    print("-------------------------------")
    print("Word Count:  " + str(num_words))

    lines = words.count(".")
    print("Sentence Count:  " + str(lines))

    letters = 0
    for w in words.split(" "):
        letters = letters + len(w)
Avgletter = letters/(num_words)
sentence_len= num_words/lines
print("Average Letter Count:  " + str(Avgletter))

print("Average Sentence Length:  " + str(sentence_len))
