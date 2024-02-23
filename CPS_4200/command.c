#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    for (int i = 2; i < argc; i++)
    {
        int num = atoi(argv[i]);
        printf("%d^2 = %d\n", num, num * num);
    }

    return 0;
}