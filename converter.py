
def fahrenheit_to_celsius(temperature):
    ''' This function will convert fahrenheit to celsius '''

    try:
        temperature = temperature.strip()
        celsius = (float(temperature) -32)* ( 5 / 9 ) 
        celsius = round(celsius, 3)  # Round to three decimal places
        return str(celsius)
    except ValueError:
        return "invalid input"

if __name__ == "__main__":
    fahrenheit= input("Temperature in Fahrenheit: ")
    print("Fahrenheit:", fahrenheit_to_celsius(fahrenheit))



