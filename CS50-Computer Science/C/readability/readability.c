#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text:" );
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    //Getting the grade:
    float L = ((float)letters / (float)words) * 100;
    float S = ((float)sentences / (float)words) * 100;
    int grade = round(0.0588 * L - 0.296 * S - 15.8);

    if(grade < 1){
        printf("Before Grade 1\n");
    }else if(grade> 16){
        printf("Grade 16+\n");
    }else{
        printf("Grade %i\n",grade);
    }

}



int count_letters(string text)
{
    int letters = 0;
    int longitud = strlen(text);
    for (int i = 0; i<longitud;i++)
    {
        if (isalpha(text[i])){
            letters ++;
        }
    }return letters;

}

int count_words(string text)
{
    int words = 1;
    int longitud = strlen(text);
    for (int i = 0; i<longitud;i++)
    {
        if (text[i] == ' '){
            words ++;
        }
    }return words;
}

int count_sentences(string text)
{
    int sentences =  0;
    int longitud = strlen(text);
    for (int i = 0; i<longitud;i++)
    {
        if (text[i] == '.' || text[i] == '!' ||text[i] == '?'  ){
            sentences ++;
        }
    }return sentences;
}
