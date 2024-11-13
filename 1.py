import math

print("Enter 2 diagonales of rhombus")

d1 = float(input("First diagonal: "))
d2 = float(input("Second diagonal: "))
s = float((1.0/2.0) * d1 * d2)

print(f"Square {round(s,3)}")


print("Task 2, enter angle: ")
alfa = float(input("Enter angle: "))
z1 = 2 * math.sin(3 * math.pi - 2 * alfa)**2 * math.cos(5 * math.pi + 2 * alfa)**2
z2 = (1/4) - (1/4)*math.sin(5/2*math.pi - 8 * alfa)

print(round(z1,3) == round(z2,3))