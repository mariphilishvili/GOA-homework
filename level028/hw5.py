sum = 0
num = int(input("enter number: "))
while num != 0:
    if num > 0:
        print("positive")
    else:
        print("ngtive")
    sum += num
    num = int(input("enter number: "))
    print("sum is:", sum)