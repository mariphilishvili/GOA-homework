#  მომხმარებელს შემოაყვანინე ასაკი, თუ ასაკინ < 18-ზე -> "შენ ხარ არასრულწლოვანი", თუ ასაკი 18 და 64 შორისაა -> "შენ ხარ სრულწლოვანი", 
# თუ ასაკი > 65-ზე -> "შენ ხარ პენსიონერი"
age = int(input("enter your age: "))
if age < 18:
    print("you are adult")
elif 18 <= age <= 64:
    print("you are adult")
else:
    print("you are old")