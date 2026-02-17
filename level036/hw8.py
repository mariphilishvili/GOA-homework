#  შექმენი ფუქნცია რომელიც მიიღებს რაღაც ტექსტს და ასევე რაღაც რიცხვს, ტექსტსში ყველა ასოა აქციე დიდად 
#და რიცხვითი მნიშვნელობა გადააქცია სტრინგის ტიპად.\
def textnumber(text, number):
    uppertext = text.upper()
    numberasstring = str(number)
    return uppertext, numberasstring

text, num_str = textnumber("hey", 123)
print(text)     
print(num_str)  
