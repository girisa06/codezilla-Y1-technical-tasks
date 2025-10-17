word = input("Enter a word: ").strip()
newWord = ""
for i in range(len(word)-1,-1,-1):
    newWord = newWord + word[i]
print("Reversed word - " + newWord)
