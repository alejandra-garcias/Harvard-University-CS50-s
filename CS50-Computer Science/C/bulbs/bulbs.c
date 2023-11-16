#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // Obtener el mensaje del usuario y su longitud
    string message = get_string("Message: ");
    int longitud = strlen(message);

    // Variables para almacenar el valor ASCII y los bits binarios
    int decimal;
    int binary[BITS_IN_BYTE] = {0};

    // Iterar sobre cada carácter del mensaje
    for (int i = 0; i < longitud; i++)
    {
        // Obtener el valor ASCII de cada carácter
        decimal = message[i];

        // Convertir el valor ASCII a su representación binaria

        for(int j = BITS_IN_BYTE - 1; j>0 ;j--)
        {
            binary[j] = decimal % 2;
            decimal = decimal / 2;
        }

        // Imprimir la representación binaria
        for (int k = 0; k < BITS_IN_BYTE; k++)
        {
            print_bulb(binary[k]);
        }
        printf("\n");
    }

    return 0;
}



void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
