#  შექმენით სტრინგის ცვლადი და ცარიელი სია. სტრინგში მყოფი დიდი ასოები გახადეთ პატარა და ამ სიაში ჩაამატეთ, 
# ხოლო სტრინგში მყოფი პატარა ასოები გახადეთ დიდი და ასევე ჩააგდეთ ამ სიაში.
# დაპრინტეთ საბოლოო სია, გამოიყენეთ while ციკლი.

text = "MaRi"
result = []
i = 0
while i < len(text):
    if text[i] == text[i].upper():
        result.append(text[i].lower())
    else:
        result.append(text[i].upper())
    i += 1
print(result)