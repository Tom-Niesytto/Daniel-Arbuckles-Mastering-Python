import math

def main():
    print(example_function('Alice',7))
    print(example_function('Bob', 5))

def example_function(name, radius):
    area = math.pi * radius ** 2
    return "The area of {} is {}".format(name, area)

if __name__ == '__main__':
    main()