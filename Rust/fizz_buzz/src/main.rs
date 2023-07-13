fn main() {
    fizz_buzz();
    // Hello
}


fn fizz_buzz() {
    let mut out_string: String;

    for i in 1..101 {
        out_string = "".to_string();
        if i % 3 == 0 {
            out_string += "Fizz";
        }
        if i % 5 == 0 {
            out_string += "Buzz";
        }
        if out_string == "" {
            out_string = i.to_string();
        }
        println!("{}", out_string);
    }
}