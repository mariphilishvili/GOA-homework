def number():
    number = float(input("შეიყვანე რიცხვი: "))

    if number > 0:
        return "დადებითია"
    elif number < 0:
        return "უარყოფითია"
    else:
        return "ნულია"
print(number())