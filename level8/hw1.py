#1) მომხმარებელს შემოატანინე ტემპერატურა (რიცხვი) და შემდეგ შეამოწმე: 
# თუ ტემპერატურა მეტია 30-ზე -> დაბეჭდე "ძალიან ცხელა!"
# თუ ტემპერატურა მეტია 20-ზე -> დაბეჭდე "სასიამოვნო ამინდია"
# თუ ტემპერატურა მეტია 10-ზე -> დაბეჭდე "ცოტა ცივა"
# თუ ტემპერატურა მეტია 0-ზე -> დაბეჭდე "ცივა, ჩაიცვი თბილად"
# სხვა შემთხვევაში -> "გაიყინები, სახლში დარჩი!"

number = int(input("Enter temperature: "))
if number > 30:
    print("it's too hot")
elif number > 20:
    ("weather is nice")
elif number > 10:
    print("it's bit cold")
elif number > 0:
    print("it's cold, dress warmly")
else:
    print("it's freezing, stay at home!")
