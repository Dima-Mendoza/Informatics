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

def seven():
    user_input = input("Enter a words: ")
    count_dict = {}
    
    for char in user_input:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    result = ""
    for char in user_input:
        if count_dict[char] > 0:
            count = count_dict[char]
            if count > 1:
                result += f"{count}{char}"
            else:
                result += char
            count_dict[char] = 0

    print(result)


def eight():
    user_inp = int(input("Please, enter a number: "))
    digit_sum = sum(int(digit) for digit in str(user_inp))

    if(user_inp % 2 == 0):
        print("Even")
    elif (user_inp % 2 != 0):
        print("Odd")
    if (digit_sum % 3 == 0):
        print("Divide by 3")

def nine():
    pass

def ten():
    user_inp = int(input("Please, enter a number: "))

    if user_inp == 0:
        print(0)
    elif user_inp == 1:
        print(1)

    a,b = 0, 1
    for _ in range(2, user_inp + 1):
        a, b = b, a+b
        
    print(b)

def eleven():
    pass

def twelve():
    pass

def thirteen():
    user_inp = int(input("PLease, enter a year: "))

    if (user_inp % 4 == 0 and user_inp % 100 != 0) or (year % 400 == 0):
        print(f"{user_inp} is leap year!")
    else:
        print(f"{user_inp} is not leap year!")

def fourteen():
    pass

def fifteen():
    pass

def sixteen():
    pass

def seventeen():
    pass

def eighteen():
    pass

def nineteen():
    pass

def twenty():
    pass


def main():
    options = {
        '1': one,
        '2': two,
        '3': three,
        '4': four,
        '5': five,
        '6': six,
        '7': seven,
        '8': eight,
        '9': nine,
        '10': ten,
        '11': eleven,
        '12': twelve,
        '13': thirteen,
        '14': fourteen,
        '15': fifteen,
        '16': sixteen,
        '17': seventeen,
        '18': eighteen,
        '19': nineteen,
        '20': twenty
    }

    print("Choose an option(1-20): ")

    choice = input("Enter number: ").strip()

    if choice in options:
        options[choice]()
    else:
        print("Something went wrong!")

if __name__ == "__main__":
    main()