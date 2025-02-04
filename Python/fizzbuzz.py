# Simple manual fizzbuzz, cumbersome to update, needs manual calculations of all possible multiplications of numbers
def fizzBuzzV1():
    for i in range(1,101):

        if i % 15 == 0:
            print("fizzbuzz")
        elif i % 5 == 0:
            print("buzz")
        elif i % 3 == 0:
            print("fizz")
        else:
            print(i)

# More usable fizzbuzz, needs only to add another if statement per new number, automatic multiplication
def fizzBuzzV2():
    for i in range(1, 101):

        out = ""

        if i % 3 == 0:
            out += "fizz"
        if i % 5 == 0:
            out += "buzz"
        if i % 7 == 0:
            out += "fuzz"
        if out == "":
            out = i

        print(out)

# Numbers are kept in a dictionary, easy to add new number to, automatic multiplication, but with nested for-loops
def fizzBuzzV3():

    numbers = {3: "fizz", 5: "buzz"}

    for i in range(1,101):

        out = ""

        for number in numbers:
            if i % number == 0:
                out += numbers[number]
        if out == "":
            out = i

        print(out)

# Same as V2, but this time recursive (woho)
def fizzBuzzV4(i):
    if i > 100:
        return

    out = ""

    if i%3 == 0:
        out += "fizz"
    if i%5 == 0:
        out += "buzz"
    if out == "":
        out = i

    print(out)

    fizzBuzzV4(i+1)

if __name__ == "__main__":
    print("\nFizzBuzz V1:\n")
    fizzBuzzV1()
    print("\nFizzBuzz V2:\n")
    fizzBuzzV2()
    print("\nFizzBuzz V3:\n")
    fizzBuzzV3()
    print("\nFizzBuzz V4:\n")
    fizzBuzzV4(1)
