def numInput(type):
    return float(input(f"Enter the {type} "))
def f_to_c(f):
    return round(5*(f-32)/9, 2)
def c_to_f(c):
    return round((c * 9/5) + 32, 2)

def program():
    i=input("What doe You want celcius to faranhite (press 1 for that) or farnhite to celcius (press 2 for that) ")
    if i == "1":
        n= numInput("farnhite")
        print(f"{n}°f in celcius is {f_to_c(n)}°C")
    elif i == "2":
        n= numInput("celcius")
        print(f"{n}°C in Fahrenheit is {c_to_f(n)}°F")
    else:
        print("Please choose a valid Operation")
        program()
program()
