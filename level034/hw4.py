#  შექმენით ფუნქცია. მომხმარებელს შემოატანინეთ წინადადების სტრინგი. დათვალე, რამდენი სიტყვის სიგრძე არის 4-ზე მეტი. 
# დაპრინტე ასეთი სიტყვების რაოდენობა.დაწერეთ ეს დავალება ორნაირად - split() ფუნქციით და split() ფუნქციის გარეშე.
def countlongwords():
    text = input("sheiyvanet winadadeba: ")
    words = text.split()   
    count = 0
    for i in words:
        if len(i) > 4:
            count += 1
    print("4ze grdzeli raodenobaa:", count)
countlongwords()