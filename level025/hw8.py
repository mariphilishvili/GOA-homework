# შექმენი list: animals = ["dog", "cat", "horse", "cow"]
# მომხმარებელს შეაყვანინე ცხოველის სახელი, თუ არსებობს  დაბეჭდე მისი index-იმ, თუ არა  "Animal not found"
animals = ["dog", "cat", "horse", "cow"]
animal = input("enter any dogs name: ")
if animal in animals:
    print("index:",animals.index(animal))
else:
    print("animal not found")