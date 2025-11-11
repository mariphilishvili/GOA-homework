#მომხმარებელს შემოატანინე ორი რიცხვი:
# --> ქულა (score)
# --> დასწრება (attendance პროცენტებში)
# შემდეგ შეამოწმე:
# თუ ქულა მეტია 80-ზე და დასწრება მეტია 90-ზე -> "შენ შესანიშნავად დაწერე გამოცდა"
# თუ ქულა მეტია 50-ზე და დასწრება მეტია 70-ზე -> "საშუალოდ დაწერე გამოცდა"
# თუ ქულა მეტია 30-ზე ან დასწრება მეტია 50-ზე -> "გაჭირვებით, მაგრამ ჩააბარე გამოცდა"
# ყველა სხვა შემთხვევაში → "ჩაიჭერი!"

number = int(input("Enter the score: "))
number2 = int(input("Enter the attemdamce: "))
if number > 0 and number2 > 90:
    print("you did excellent")
elif number > 50 and number2 > 70:
    print("you did okay")
elif number > 30 or number2 > 50:
    print("you passed with difficulty")
else:
    print("you failed")

