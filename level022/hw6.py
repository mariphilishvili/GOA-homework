# ტერმინალში გამკოიუტანეთ ყველა ლუწი რიცხვის ჯამი გამოიყენეთ ინდექსინგი


data = [10, 23, 35, 42, 58, 61]
sum = 0
for i in range(len(data)):
    if data[i] % 2 == 0:
        sum += data[i]
        print(sum)
