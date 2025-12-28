numbers = []
while True:
    number = input("enter number or 'stop': ")
    if number == "stop":
        print("break")
    num = int(number)
    if num < 50:
        numbers.insert(0, num)
    else:
        numbers.append(num)
        print("ganaxlebuli sia:",numbers)