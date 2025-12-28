# შექმენი list: nums = [1, 2, 3, 4] მომხმარებელს შეაყვანინე: ინდექსი და რიცხვი, თუ ინდექსი 
# list-ის საზღვრებშია გამოიყენე insert() ჩასამატებლად, თუ ინდექსი ლისტზე დიდია მაშინ გამოიყენე append()
nums = [1, 2, 3, 4]
index = int(input("enter index: "))
if 0 <= index < len(nums):
    nums.insert(index,nums)
else:
    nums.append(nums)
print("ganaxlebuli sia:",nums)