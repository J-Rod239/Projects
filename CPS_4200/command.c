#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int numIntegers = atoi(argv[1]);
    if (argc != numIntegers + 2)
    {
        printf("Error: You have to enter three integers.\n");
        return 1;
    }
    for (int i = 2; i < argc; i++)
    {
        int num = atoi(argv[i]);
        printf("%d^2 = %d\n", num, num * num);
    }

    return 0;
}