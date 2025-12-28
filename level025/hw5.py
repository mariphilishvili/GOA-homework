# შექმენი ნებისმიერი list 5 ელემენტით, მომხმარებელს ჰკითხე: გინდა list-ის გასუფთავება?
# (yes/no), თუ პასუხი "yes"  გამოიყენე clear(), ბოლოს დაბეჭდე list
items = ["apple", "banana", "orange", "grape", "pear"]
answer = input("გინდა list-ის გასუფთავება? (yes/no): ")
if answer == "yes":
    items.clear()
    print(items)