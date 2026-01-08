# შექმენი ცარიელი სია. მომხმარებელს შემოაყვანინე რიცხვები, 
# თუ რიცხვი უკვე არსებობს სიაში შეწყვიტე შეყვანა, სხვა შემთხვევაში დაამატე რიცხვები სიაში, ბოლოს დაბეჭდე მთლიანი სია
numbers = []
while True:
    number = input("enter any number: ")
    num = int(number)
    if num in numbers:
        break
    numbers.append(num)
    print("unikaluriricxvebi:",numbers)