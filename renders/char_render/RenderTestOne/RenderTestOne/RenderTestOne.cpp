// RenderTestOne.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

const int SW = 32;
const int SH = 16;
void zoom_wall(char pattern[SH][SW], float zoom) {
    char new_pattern[SH][SW];
    int new_SH = (int)(zoom * SH);
    int new_SW = (int)(zoom * SW);
    int off_y = (int)((SH - new_SH) / 2);
    int off_x = (int)((SW - new_SW) / 2);

    for (int i = 0; i < SH; i++) {
        for (int j = 0; j < SW; j++) {
            if ((i < off_y) || (i >= off_y + new_SH)) {
                new_pattern[i][j] = 32;
            }
            else {
                if ((j < off_x) || (j >= off_x + new_SW)) {
                    new_pattern[i][j] = 32;
                }
                else {
                    new_pattern[i][j] = pattern[i][j];
                } 
            }
        }
    }


    
    for (int i = 0; i < SH; i++) {
        for (int j = 0; j < SW; j++) {
            std::cout << new_pattern[i][j];
        }
        std::cout << '\n';
    }
     
}

int main()
{
    char test_mtr[SH][SW];
    for (int i = 0; i < SH; i++) {
        for (int j = 0; j < SW; j++) {
            if ((i%4>1)* (j % 4>1) || (i%4<=1)*(j%4<=1))
            {
                test_mtr[i][j] = 176;
            }
            else {
                test_mtr[i][j] = 178;
            }
        }
        std::cout << '\n';
    }
    for(int i = 0; i < 1000;i++){
        std::cout << ((float)i / 1000) << '\n';
        zoom_wall(test_mtr, (float)i/1000);
        system("CLS");
    }
    
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
