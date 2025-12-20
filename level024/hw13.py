# შექმენი ცვლადი --> ჰიდროელექტროსადგური
# მომხმარებელს შემოატანინე ორი რიცხვი0  დან 19 ის ჩათვლით ორივე

# შენი დავალებაა რომ ტერმინალში გამოიტანო ახალი სტრინგი 

# მოახდინე სლაისინგი --> start იყოს პირველი რიცხვი და end იყოს მეორე შემოტანილი რიცხვი
word = "ჰიდროელექტროსადგური"
number1 = int(input("pick first number out of 0-19: "))
number2 = int(input("pick second number out of 0-19: "))
if number1 > number2:
    number1, number2 = number2, number1
sliced = word[number1:number2]
print(sliced)
