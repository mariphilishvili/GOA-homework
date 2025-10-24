#მომხმარებელს შემოატანინე:
# --> ტემპერატურა (temp)
# --> არის თუ არა წვიმა (rain) – მომხმარებელმა შეიყვანოს "yes" ან "no"
# შემდეგ შეამოწმე:
# თუ ტემპერატურა მეტია 25-ზე და rain == "no" -> "შესანიშნავი ამინდია სასეირნოდ!"
# თუ ტემპერატურა მეტია 25-ზე და rain == "yes" -> "ცხელი და წვიმიანია, ჩაფხუტი დაგჭირდება!"
# თუ ტემპერატურა ნაკლებია 10-ზე ან rain == "yes" -> "სჯობს სახლში დარჩე"
# სხვა შემთხვევაში -> "სასიამოვნო ამინდია"
number =int(input("Enter the temperature: "))
rain = input("Is it raining? (yes/no): ")

if number > 25 and rain == "no":
    print("it's a perfect day for a walk!")
elif number > 25 and rain == "yes":
    print("it's hot and rainy, you'll need an umbrella!")
elif number < 10 or rain == "yes":
    print("better stay at home.")
else:
    print("the weather is nice.")

