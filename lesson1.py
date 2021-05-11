import sys
import flake8

print(sys.argv)

# import lesson_package.units
from lesson_package import units

r = units.say_twice('hello')
print(r)

lambda x: x*2

def main():
  print('hello!')

if __name__ == '__main__':
  main()