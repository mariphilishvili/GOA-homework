# შექმენი ფუქნცია რომელიც მიიღებს რიცხვების სიას [3, 7, 1, 9] და დააბრუნებს ყველაზე დიდ რიცხვს
def find_max(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest