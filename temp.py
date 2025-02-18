print("Enter the temperature you want to convert")  
choice = input("Celsius to Fahrenheit (F) or Fahrenheit to Celsius (c)...? ")  
print("________________________________________________________")  
if choice.lower() == 'c':   
    celsius = float(input("Enter your temperature in Celsius: "))  
    fahrenheit = (celsius * 9 / 5) + 32  
    print(f"{celsius}°C is equal to {fahrenheit}°F")  

elif choice.lower() == 'f':    
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))  
    celsius = (fahrenheit - 32) * 5 / 9  
    print(f"{fahrenheit}°F is equal to {celsius}°C")  

else:  
    print("Wrong choice.")