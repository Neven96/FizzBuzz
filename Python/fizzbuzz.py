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


if __name__ == "__main__":
    print("\nFizzBuzz V1:\n")
    fizzBuzzV1()
    print("\nFizzBuzz V2:\n")
    fizzBuzzV2()
    print("\nFizzBuzz V3:\n")
    fizzBuzzV3()