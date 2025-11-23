#შექმენი ცვლადი და შეინახე შენი პაროლი(string) მომხმარებელს შემოატანინე პაროლი
#სანამ შენი პაროლი არ უდრის მომხმარებლის მიერ შემოტანილ პაროლს
#მომხმარებელს თავიდან შემოატანინე პაროლი რომ გაარტყას შენ პაროლს
#დაპრინტე "სწორია გაარტყი"

password = "ertiorisami123"
guesspassword = input("guess password: ")
while password !=  guesspassword:
    guesspassword = input("guess password: ")
print("gaartyi")
