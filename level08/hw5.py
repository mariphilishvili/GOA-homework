#მომხმარებელს შემოატანინე:
# --> მომხმარებლის სახელი (username)
#
# --> პაროლი (password)
# შეამოწმე:
# თუ მომხმარებელი არის "admin" და პაროლი არის 'superSecretPassword' → "მოგესალმები, ადმინ!"
# თუ მომხმარებელი "guest" და პაროლი არის "1234" → "მოგესალმები, სტუმარო!"
# სხვა შემთხვევაში → "მომხმარებელი არ მოიძებნა!

username= input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "superSecretPassword":
    print("welcome, admin!")
elif username == "guest" and password == "1234":
    print("welcome, guest!")
else:
    print("user not found!")