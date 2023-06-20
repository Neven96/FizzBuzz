def FizzBuzz()
    out = ""
    for i in 1..100 do
        out = ""
        if i % 3 == 0
            out += "Fizz"
        end
        if i % 5 == 0
            out += "Buzz"
        end
        if out == ""
            out = i
        end
        puts out
    end
end

FizzBuzz()