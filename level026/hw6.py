# მომხმარებელს შემოაყვანინე რიცხვები, შექმენი ორი სია დადებითი 
# და უარყოფითი სიებისთვის, დადებითი რიცხვები დაამატე დადებითი რიცხვებისთვის განკუთვნილ სიაში, უარყოფითი რიცხვები კი პირიქით

numbers = []
positive = []
negative = []
while True:
    number = input("enter number or 'stop': ")
    if number == "stop":
        break
    num = int(number)
    numbers.append(num)
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
        print("all numbers:", numbers)
        print("positive numbers:", positive)
        print("negative numbers:", negative)
