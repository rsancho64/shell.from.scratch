#include <stdio.h>
#include <string.h>

#define BUFFERSIZE 10

int main (int argc, char *argv[])
{
    char buffer[BUFFERSIZE];
    printf("Enter a message: \n");
    while(fgets(buffer, BUFFERSIZE , stdin) != NULL)
    {
        printf("%s\n", buffer);
    }
    return 0;
}