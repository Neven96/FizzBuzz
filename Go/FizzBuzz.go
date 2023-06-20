package main

import (
	"fmt"
	"strconv"
)

func main() {
	fmt.Println("FizzBuzz V1:")
	fizzBuzzV1()
	fmt.Println("FizzBuzz V2:")
	fizzBuzzV2()
}

func fizzBuzzV1() {
	for i := 1; i <= 100; i++ {
		if i%15 == 0 {
			fmt.Println("FizzBuzz")
		} else if i%5 == 0 {
			fmt.Println("Buzz")
		} else if i%3 == 0 {
			fmt.Println("Fizz")
		} else {
			fmt.Println(i)
		}
	}
}

func fizzBuzzV2() {
	var out string = ""
	for i := 1; i <= 100; i++ {
		out = ""
		if i%3 == 0 {
			out += "Fizz"
		}
		if i%5 == 0 {
			out += "Buzz"
		}
		if out == "" {
			out = strconv.Itoa(i)
		}
		fmt.Println(out)
	}
}
