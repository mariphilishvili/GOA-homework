# შექმენი ფუნქცია რომელიც მიიღებს სიტყვების სიას და დააბრუნებს მხოლოდ იმ სიტყვებს რომლებიც იწყება დიდი ასოთი
def capitals(words):
    result = []
    for word in words:
        if word and word[0].isupper():
            result.append(word)
    return result
words = ["tbilisi", "qalaqi", "Georgia", "world", "Hello"]
print(capitals(words))