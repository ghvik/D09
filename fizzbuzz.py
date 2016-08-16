# Fizzbuzz

def fizzbuzz():
    """Prints fizz or buzz depending on the index"""
    for n in range(1,101):
        if n % 15 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)

def fizzbuzz2():
    """Prints fizz or buzz depending on the index"""
    msg = ""
    for n in range(1,101):
        if n % 3 == 0:
            msg += "Fizz"
        if n % 5 == 0:
            msg += "Buzz"
        else:
            print(msg or n)
def main():
    fizzbuzz()
    
if __name__ == "__main__":
    main()