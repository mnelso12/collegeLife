// for choosing between top choices for summer internship

#include <iostream>
#include <cmath>
#include <cstdlib>
#include <string>
#include <time.h>

using namespace std;

int main()
{
    int countProtiviti = 0, countAbbVie = 0;
    int i=0;
    int myInternship;
    srand(time(NULL)); 
    while (i<1000000000)
    {

        myInternship = rand() % 100;
        //cout << myInternship << endl;

        if (myInternship >= 50)
        {
            countProtiviti++;
        }
        else
        {
            countAbbVie++;
        }
        i++;
    }
    string name; 
    cout << "Protiviti: " << countProtiviti << endl;
    cout << "AbbVie: " << countAbbVie << endl << endl;
    if (countProtiviti > countAbbVie)
    {
        name = "Protiviti";
    }
    else
    {
        name = "AbbVie";
    }
    cout << "you chose: " << name << endl;

    return 0;
}
