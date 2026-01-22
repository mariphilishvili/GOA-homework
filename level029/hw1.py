list1 = ["mari", 15, 2.3, True]
count = 0
for i in range(len(list)):
    if type(list[i]) == str:
        count += 1
print(f"string is in {count} list")
