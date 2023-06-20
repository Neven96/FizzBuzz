public class FizzBuzz {
    public static void main(String[] args) {
        System.out.println("FizzBuzzV1:");
        FizzBuzzV1();
        System.out.println("FizzBuzzV2:");
        FizzBuzzV2();
    }

    public static void FizzBuzzV1() {
        for (int i = 1; i <= 100 ; i++) {
            if (i % 15 == 0) {
                System.out.println("FizzBuzz");
            } else if (i % 3 == 0) {
                System.out.println("Fizz");
            } else if (i % 5 == 0) {
                System.out.println("Buzz");
            } else {
                System.out.println(i);
            }
        }
    }

    public static void FizzBuzzV2() {
        String out = "";

        for (int i = 1; i <= 100; i++) {
            out = "";
            if (i % 3 == 0) {
                out += "Fizz";
            }
            if (i % 5 == 0) {
                out += "Buzz";
            }
            if (i % 7 == 0) {
                out += "Fuzz";
            }
            if (out == "") {
                out = String.valueOf(i);
            }
            System.out.println(out);
        }
    }
}
