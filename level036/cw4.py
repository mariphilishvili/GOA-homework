def numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
nums = [10,20,30,100,200,500]
result = numbers(nums)
print(result)