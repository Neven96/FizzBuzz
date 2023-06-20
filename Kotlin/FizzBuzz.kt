fun main() {
    println("FizzBuzzV1:")
    fizzBuzzV1()
    println("FizzBuzzV2:")
    fizzBuzzV2()
}

fun fizzBuzzV1() {
    for (i in 1..100) {
        if (i % 15 == 0) {
            println("FizzBuzz")
        } else if (i % 5 == 0) {
            println("Buzz")
        } else if (i % 3 == 0) {
            println("Fizz")
        } else {
            println(i)
        }
    }
} 

fun fizzBuzzV2() {
    var out = ""
    for (i in 1..100) {
        out = ""
        if (i % 3 == 0) {
            out += "Fizz"
        }
        if (i % 5 == 0) {
            out += "Buzz"
        }
        if (out == "") {
            out = i.toString()
        }
        println(out)
    }
}