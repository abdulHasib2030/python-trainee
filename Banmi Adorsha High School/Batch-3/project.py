
# a = int(input("Enter a number: "))
# sign = input("Enter a sign: ")
# b = int(input("Enter another number: "))

# if sign == '+':
#     print("Summation result", a + b)

# elif sign == '-':
#     print("Subtration result", a - b)

# elif sign == '*':
#     print("Muliplication result", a * b)

# elif sign == '/':
#     print("Division result", a / b)

# elif sign == '%':
#     print("Modules result", a % b)

# else:
#     print("Invalid number")


import turtle
import colorsys
t = turtle.Turtle()
s = turtle.Screen().bgcolor('gray')
t.speed(140)
n = 70
h = 0
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1/n
    t.color(c)
    t.left(1)
    t.fd(1)
    for j in range(2):
        t.left(2)
        t.circle(100)
















