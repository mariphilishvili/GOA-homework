# შექმენი list: fruits = ["apple", "banana", "apple", "orange"] მომხმარებელს შეაყვანინე ხილი,
# თუ list-ში უკვე არის ეს ხილი remove()-ით წაშალე მხოლოდ პირველი შემხვედრი, თუ არ არის ლისტში მაშინ დაბეჭდე შესაბამისი შეტყობინება
fruits = ["apple", "banana", "apple", "orange"]
fruit = input("enter your fruit: ")
if fruit in fruits:
    fruits.remove(fruit)
    print("იყო სიაში და წაიშალა")
else:
    print("არ იყო სიაში")
    print(fruits)