sentence = input("Enter a sentence: ")

words = sentence.split()

freq = {}

for word in words:
    if word not in freq:
        freq[word] = 1
    else:
        freq[word] += 1

print("\nWord Frequencies:")

for word in freq:
    print(word, ":", freq[word])
