# შექმენი ცარიელი list, მომხმარებელს 5-ჯერ შეაყვანინე რიცხვი,
# ყველა დაამატე list-ში და საბოლოოდ for loop-ის გამოყენებით დააჯამე რიცხვები რომელიც გექნება ლისტში
nums = []
for i in range(5):
    num = int(input("sheiyvane ricxvi: "))
    nums.append(num)

total = 0
for num in nums:
    total += num
    print("ricxvebis jami aris:", total)