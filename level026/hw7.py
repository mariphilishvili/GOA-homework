numbers = []
while True:
    number = input("enter number 'stop': ")
    if number == "stop":
        print(number)
    num = int(number)
    numbers.append(num)

    i = 0
    while i < len(numbers) - 1:
        if numbers[i] + numbers[i+1] < 50:
            numbers.pop(i+1)
    else:
        i += 1
        print("საბოლოო სია:", numbers)