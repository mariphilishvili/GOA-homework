# შექმენით ფუნქცია. შექმენით რიცხვებით სავსე სია, დაბეჭდეთ სიის უდიდესი ელემენტი. 
# არ გამოიყენოთ max() ფუნქცია, გამოიყენეთ for ციკლი. გამოიძახეთ ფუნქცია.
def newlist():
    list1 = [5, 13, 40, 15, 70, 55]
    biggest = list1[0]
    for i in list1:
        if i > biggest:
            biggest = i
    print("udidesi elementi:", biggest)
newlist()