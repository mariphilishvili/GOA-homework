def sum_of_digits():
    text = input("sheikvanet teqsti: ")
    total = 0
    for i in range(len(text)):
        if text[i].isdigit():  # შემოწმება, არის თუ არა ციფრი
            total += int(text[i])
    print(total)
sum_of_digits()