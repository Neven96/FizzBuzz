#include <iostream>
#include <string>

using namespace std;

void FizzBuzz() 
{
    string out;
    for (int i = 0; i <= 100; i++)
    {
        out = "";
        if (i % 3 == 0)
        {
            out += "Fizz";
        }
        if (i % 5 == 0)
        {
            out += "Buzz";
        }
        if (out == "")
        {
            out = std::to_string(i);
        }
        std::cout << out << "\n";
    }
    
}

int main()
{
    FizzBuzz();
}