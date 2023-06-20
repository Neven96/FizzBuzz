class FizzBuzz
{
    static void Fizzbuzz()
    {
        string outString;

        for (int i = 1; i <= 100; i++)
        {
            outString = "";
            if (i % 3 == 0)
            {
                outString += "Fizz";
            }
            if (i % 5 == 0)
            {
                outString += "Buzz";
            }
            if (outString == "")
            {
                outString = i.ToString();
            }
            Console.WriteLine(outString);
        }
    }

    static void Main()
    {
        Fizzbuzz();
    }
}
