#Temperature conversion - C TO F AND F TO C
print("Welcome to temperature converter!")

Unit = input("Enter unit (F) - C TO F or (C) F TO C : ")
T = float(input("Enter temperature : "))

if Unit == "F" or Unit == "f" :
    print("You selected C° TO F°")
    result  = round((T * 1.8 + 32) , 2)
    Unit = "F°"

elif Unit == "C" or Unit == "c" :
    print("You selected F° to C°")
    result = round(((T - 32) * (5/9))  , 2)


print(f"Result : {result}")
