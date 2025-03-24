#include <stdio.h>
#include <string.h>

#include "fizzbuzz.h"

void fizzbuzz()
{
    char output[20] = "";
    for (int i = 1; i <= 100; i++)
    {
        strcpy(output, "");
        if (i % 3 == 0)
        {
            strcat(output, "fizz");
        }

        if (i % 5 == 0)
        {
            strcat(output, "buzz");
        }

        if (output[0] == '\0')
        {
            sprintf(output, "%d", i);
        }

        printf("%s\n", output);
    }
}