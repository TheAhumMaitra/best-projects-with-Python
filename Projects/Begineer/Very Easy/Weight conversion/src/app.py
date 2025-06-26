#Weight conversion
print("Welcome to weight converter \n\n")

weight =int(input("Enter your weight : "))

conversion = input("Conversion unit Kilogram to (P)ound or Pound to (K)ilogram :- \n Eg : P (KG TO POUND) OR K (POUND TO KILOGRAM)\n\n")

if conversion == "P" or conversion == "p" :
    print("You selected - Kilogram to Pound")
    converted = round((weight  * 2.20462262) , 2)
    print(f"Converted value : {converted} in Pounds")

elif conversion == "K" or conversion == "k" :
    print("You selected - Pound to Kilogram")
    converted = round((weight  % 2.20462262) , 2)
    print(f"Converted value : {converted} in KG(s)")


else :
    print(f"{conversion} unit not found! ")
    print("Eg : P (KG TO POUND) OR K (POUND TO KILOGRAM)")
