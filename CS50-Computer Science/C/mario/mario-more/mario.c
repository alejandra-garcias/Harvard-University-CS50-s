#include <cs50.h>
#include <stdio.h>

int main(void)
{
// Get height

    int height, row, column, space;

    do
    {
        height = get_int("How many blocks would you like? \n");

    } while (height < 1 || height>8);

    // Make block pattern

    for (row  = 0; row < height; row++)
    {
        for(space = 0; space < height - row - 1 ; space++){

            printf(" ");

        }

        for(column = 0; column <= row; column++){

            printf("#");

        }

        printf("  ");

        for(column = 0; column <= row; column++){

            printf("#");

        }

        printf("\n");
    }
}
