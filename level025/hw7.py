# შექმენი list: letters = ["a", "b", "c", "d", "e"] მომხმარებელს შეაყვანინე ინდექსი,
#  pop()-ით წაშალე ამ ინდექსზე მდგომი ელემენტი, დაბეჭდე წაშლილი ელემენტი და list1
letters = ["a", "b", "c", "d", "e"]
index = int(input("sheiyvane indexi: "))
if 0 <= index <len(letters):
    removed = letters.pop(index)
    print("washlili elementi")
else:
    print("araswori index")
    print("ganaxlebuli sia")