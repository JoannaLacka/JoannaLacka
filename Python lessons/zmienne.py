# Typy zmiennych:
# int - typ całkowty
# float - typ rzeczywisty
# string - ciągi znaków
# bool - typ logiczny
# complex - typ dla liczb zespolonych

# snake case np name_surname

age = 31
name = "Joanna"

print(name)
print(age)

# nadpisanie zmiennej
number_of_points = 0
print(number_of_points)
number_of_points = 7
print(number_of_points)

points = 0
points = "two"
print(points)

# zmiana typu zmiennych castowanie

# x = str(3)   
# y = int(3)
# z = float(3)

# print(x)
# print(y)
# print(z)

x = 2.0
y = int(x)
print(y)

# sprawdzanie typu zmiennej używamy metody type
number = 5
name = "Joanna"
print(type(number))
print(type(name))
