numbers = []
positive = []
negative = []
while True:
    number = input("enter number or 'stop': ")
    if number == "stop":
        print("break")
    num = int(number)
    numbers.append(num)
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
        print("all numbers:",numbers)
        print("positive numbrs:",positive)
        print("negative numbers:",negative)
