#include <cs50.h>
#include <stdio.h>
int main(void)
{
    // Prompt for start size
    int start_population;
    do{
        start_population = get_int("What is the starting population? ");
    }
    while (start_population < 9);

    // Prompt for end size
    int end_population;
    do{
       end_population = get_int("What is the ending population? ");
    }
    while (end_population < start_population);

    // Calculate number of years until we reach threshold
    int years =0;
    while(start_population<end_population){
       start_population += start_population / 3 - start_population / 4;
       years++;
    }

    // Print number of years
    printf("Years: %i \n",years);
}
