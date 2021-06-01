// RenderTestOne.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

const int SW = 16;
const int SH = 32;
void zoom_wall(char pattern[SW][SH], float zoom) {
    for (int i = 0; i < SW; i++) {
        for (int j = 0; j < SH; j++) {
            std::cout << pattern[i][j];
        }
        std::cout << '\n';
    }
     
}

int main()
{
    char test_mtr[SW][SH];
    for (int i = 0; i < SW; i++) {
        for (int j = 0; j < SH; j++) {
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
    zoom_wall(test_mtr, 10);
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
