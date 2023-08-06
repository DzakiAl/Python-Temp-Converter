print("Wellcome to Temperature Converter Program")
print("Please choose which temparature unit did you want to convert:")
print("1. Celcius to Fahrenheit")
print("2. Fahrenheit to Celcius")

choice = int(input("Your input: "))

if choice == 1 :
    celcius = int(input("Please enter a celcius temperature: "))
    fahrenheit = (celcius * 9/5) + 32
    print(fahrenheit)
elif choice == 2 :
    fahrenheit = int(input("Please enter a fahrenheit temparature: "))
    celcius = (fahrenheit -32) * 5/9
    print(celcius)
else:
    print("Please enter right number")