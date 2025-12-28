# შექმენი ცარიელი list მომხმარებელს შემოაყვანინე რიცხვები მანამ სანამ არ დაწერს "stop", 
# ყველა რიცხვი დაამატე ლისთში append()ის გამოყენებით და საბოლოოდ დაბეჭდე ლისთი
numbers = []
while True:
    number = input("enter number or 'stop' for break: ")
    if number == "stop":
        print("break")
    else:
        numbers.append(number)
        print("your numbers:",numbers)