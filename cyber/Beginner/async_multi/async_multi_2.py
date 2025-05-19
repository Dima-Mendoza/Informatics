import concurrent.futures

def square(number):
    return number * number

def cube(number):
    return number * number * number

numbers = []

while True:
    user_inp = input("Enter a number or enter q to exit: \n")
    if user_inp == "q":
        break
    numbers.append(int(user_inp))

print(f"\nList of numbers: {numbers}")

with concurrent.futures.ThreadPoolExecutor() as executor:
    squares = executor.map(square, numbers)
    cubes = executor.map(cube, numbers)

for result in squares:
    print(result)

for result in cubes:
    print(result)