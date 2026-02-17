# შექმენი ფუქნცია რომელიც მიიღებს რაღაც ტექსტს და დაითვლის ამ ტექსტში ხმოვნების რაოდენობას
def count(text):
    xmovnebi = "აეიოუ"
    count = 0
    for char in text.lower():
        if char in xmovnebi:
            count += 1
    return count
print(count("გამარჯობა"))  