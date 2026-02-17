# შექმენი ფუქნცია რომელიც იღებს რიცხვების სიას და აბრუნებს მათ საშუალოს
def average(numbers):
    if not numbers:
        return 0  
    return sum(numbers) / len(numbers)
print(average([3, 7, 1, 9]))  