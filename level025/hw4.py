#  შექმენი list: colors = ["red", "blue", "green", "yellow"]
# მომხმარებელს შეაყვანინე ფერი, თუ არსებობს  დაბეჭდე მისი index(), თუ არა  დაბეჭდე "Not found"
colors = ["red", "blue", "green", "yellow"]
color = input("enter your color: ")
if color in colors:
    print(colors.index(color))
else:
    print("not found")