numbers = []
while True:
    number = input("enternumber or 'stop': ")
    if number == "stop":
        print("break")
    num = int(number)
    if num > 0:
        numbers.append(num)
        print("dadebiti ricxvebi:",numbers)