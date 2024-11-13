import math
import string

def one():

    dic_eng = "aeiouAEIOU"
    vowel = 0
    cons = 0

    user_inp = input("Please, enter a word: ")
    
    for char in user_inp:
        if char.isalpha():
            if char.lower() in dic_eng:
                vowel += 1
            else:
                cons += 1
    print(f"Vowels: {vowel}, cons: {cons}")

def two():
    user_degree = float(input("Please, enter a degree: "))

    degrees = int(user_degree)

    decimal_minutes = (user_degree - degrees) * 60
    minutes = int(decimal_minutes)

    seconds = (decimal_minutes - minutes) * 60

    print(f"{user_degree}° = {degrees}° {minutes}' {seconds}\"")

def three():
    pass

def four():
    a, b, c = [float(input(f"Enter 3 numbers {_}: ")) for _ in ['a', 'b', 'c']]

    discriminant = b**2 - 4*a*c

    if (discriminant > 0):
        x1 = (-b + math.sqrt(discriminant))
        x2 = (-b - math.sqrt(discriminant))
        print(f"X1 is {x1}, X2 is {x2}")
        exit()

    elif discriminant == 0:
        x = -b / (2*a)
        print(f"X is: {x}")

    else:
        print("No squares")

def five():
    pass

def six():
    pass



def main():
    options = {
        '1': one,
        '2': two,
        '3': three,
        '4': four,
        '5': five,
        '6': six
    }

    print("Choose an option(1-20): ")

    choice = input("Enter number: ").strip()

    if choice in options:
        options[choice]()
    else:
        print("Something went wrong!")

if __name__ == "__main__":
    main()