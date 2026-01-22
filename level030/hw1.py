#  შექმენით სახელებით სავსე სია, თუ სიტყვის ყველა ასო არის პატარა და პირველი ასო არის d, მაშინ ახალ სიაში ჩაამატეთ სახელი "NIKA", 
# თუ სიტყვის ყველა ასო არის დიდი ან იწყება ასო K-თი, მაშინ სიაში ჩაამატეთ სახელი 
# "GOGA", სხვა შემთხვევაში სიაში ჩაამატეთ სიტყვა "ლიდერი". დაპრინტეთ მიღებული სია.
names = ["davit", "DATO", "kaxa", "giorgi", "dato", "Koba", "nika"]
list1 = []
for word in names:
    if word == word.lower() and word[0] == "d":
        list1.append("NIKA")
    elif word.isupper() or word[0] == "K":
        list1.append("GOGA")
    else:
        list1.append("leader")
print(list1)