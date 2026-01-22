words = ["apple", "banana", "kiwi", "orange", "fig", "melon", "pear"]
i = 0
while i < len(words):
    if len(words[i]) > 5 or i % 2 == 1:
        words.remove(words[i])
    else:
        i += 1
print(words)