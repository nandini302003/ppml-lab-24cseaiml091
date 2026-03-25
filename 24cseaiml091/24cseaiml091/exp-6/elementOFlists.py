sentence = input("Enter a sentence: ")

list1 = sentence.split()

print("\nWords in the list with their lengths:\n")
for word in list1:
    print(f"{word} - Length: {len(word)}")