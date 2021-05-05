import sys
print(sys.argv)

# import lesson_package.units
from lesson_package import units

r = units.say_twice('hello')
print(r)