#include <stdio.h>
#include <string.h>

int main()
{

    int num;
    char nombre[10];

    // un entero
    // printf("Introduce un número: ");
    // scanf("%i", &num);
    // printf("Has tecleado el número %i\n", num);

    // un string, pero un solo token (palabra)
    // printf("introduce un string: ");
    // scanf("%s", nombre);
    // printf("Has tecleado: %s\n", nombre);

    // puts-gets
    // char cadena[50];
    // puts("Escriba un texto:");
    // gets(cadena);
    // puts("El texto escrito es:");
    // puts(cadena);

    #define BUFFERSIZE 50

    char comando[BUFFERSIZE];
    char *p;
    const char s[2] = " "; // UNICO SEPARADOR: ESPACIO EN BLANCO   
    char *token0;    

    for (;;)
    {
        printf("? ");
        p = fgets(comando, BUFFERSIZE, stdin);
        if (p)
        {
            // puts("echo");
            
            // puts(comando); 
            // TO DO: puts(eval(comando)) ...

            /* first token */
            token0 = strtok(comando, s);
            printf("tok: %s\n", token0 );            

            // TODO: imprimir los demas tokens

        }
        // else
        //     puts("comando vacio");
    }
}