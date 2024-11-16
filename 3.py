import math
import string
import random

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
    user_choice = int(input("Please, choice: 1 - direct geodetic problem 2- inverse geodetic problem"))

    if (user_choice == int(1)):
        pass
    elif(user_choice == int(2)):
        pass
    else:
        print(f"You write: {user_choice}")

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
    dictionary = {
        'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з',
        'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д',
        'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь',
        'Q': 'Й', 'W': 'Ц', 'E': 'У', 'R': 'К', 'T': 'Е', 'Y': 'Н', 'U': 'Г', 'I': 'Ш', 'O': 'Щ', 'P': 'З',
        'A': 'Ф', 'S': 'Ы', 'D': 'В', 'F': 'А', 'G': 'П', 'H': 'Р', 'J': 'О', 'K': 'Л', 'L': 'Д',
        'Z': 'Я', 'X': 'Ч', 'C': 'С', 'V': 'М', 'B': 'И', 'N': 'Т', 'M': 'Ь'
    }

    user_text = input("Please, enter text: ")
    result = []

    for char in user_text:
        if (char in dictionary):
            result.append(dictionary[char])
        else:
            result.append(char)

    print(''.join(result))

def six():

    a, b, c = [int(input(f"Please, enter 3 sides of triangle, {_} is: ")) for _ in ['a', 'b', 'c']]

    if a <= 0 or b <= 0 or c <= 0:
        print("Triangle doesnt exist")
    
    if a + b <= c or a + c <= b or b + c <= a:
        print("Triangle doesnt exist")
    
    a, b, c = sorted([a, b, c])
    
    if(a**2 + b**2 == c**2): print("Triangle is right")
    else: print("Triangle is not right")

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
    bot_number = random.randrange(1,100,1)
    user_choice = 0

    while (user_choice != bot_number):
        user_choice = int(input("Enter a number between 1 to 100: "))
        print ("Less") if (user_choice > bot_number) else print("More")
    print(f"Congrulations! The number is {bot_number}")

def twelve():
    user_choice = int(input("Choice 1 - Binary 2 - Deciminal: "))

    if(user_choice == int(1)):
        user_input = input("ENter a binary number: ")
        result = int(user_input,2)
        print(f"The binary number {user_input} in deciminal is {result}")
    elif(user_choice == int(2)):
        user_input = int(input("Enter a number: "))
        result = bin(int(user_input))[2:]
        print(f"The deciminal number {user_input} in binary is {result}")

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