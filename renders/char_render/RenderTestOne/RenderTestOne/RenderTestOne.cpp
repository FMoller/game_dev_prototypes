// RenderTestOne.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#define NOMINMAX
#define WIN32_LEAN_AND_MEAN
#include <Windows.h>
#include <iostream>

const int SW = 15;
const int SH = 15;

void cls()
{
    // Get the Win32 handle representing standard output.
    // This generally only has to be done once, so we make it static.
    static const HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);

    CONSOLE_SCREEN_BUFFER_INFO csbi;
    COORD topLeft = { 0, 0 };

    // std::cout uses a buffer to batch writes to the underlying console.
    // We need to flush that to the console because we're circumventing
    // std::cout entirely; after we clear the console, we don't want
    // stale buffered text to randomly be written out.
    std::cout.flush();

    // Figure out the current width and height of the console window
    if (!GetConsoleScreenBufferInfo(hOut, &csbi)) {
        // TODO: Handle failure!
        abort();
    }
    DWORD length = csbi.dwSize.X * csbi.dwSize.Y;

    DWORD written;

    // Flood-fill the console with spaces to clear it
    FillConsoleOutputCharacter(hOut, TEXT(' '), length, topLeft, &written);

    // Reset the attributes of every character to the default.
    // This clears all background colour formatting, if any.
    FillConsoleOutputAttribute(hOut, csbi.wAttributes, length, topLeft, &written);

    // Move the cursor back to the top left for the next sequence of writes
    SetConsoleCursorPosition(hOut, topLeft);
}

// x is the column, y is the row. The origin (0,0) is top-left.
void setCursorPosition(int x, int y)
{
    static const HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);
    std::cout.flush();
    COORD coord = { (SHORT)x, (SHORT)y };
    SetConsoleCursorPosition(hOut, coord);
}


void zoom_wall(char pattern[SH][SW], float zoom) {
    char new_pattern[SH][SW];
    float f_SH = (zoom * SH);
    float f_SW = (zoom * SW);
    int new_SH = (int)f_SH;
    int new_SW = (int)f_SW;

    if (SH % 2 == 0) {
        if (new_SH % 2 != 0) new_SH -= 1;
    }
    else {
        if (new_SH % 2 == 0) new_SH -= 1;
    }
    if (new_SH < 0) new_SH = 0;
    if (SH % 2 == 0) {
        if (new_SW % 2 != 0) new_SW -= 1;
    }
    else {
        if (new_SW % 2 == 0) new_SW -= 1;
    }
    if (new_SW < 0) new_SW = 0;

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
    for(int i = 0; i < 500;i++){
        std::cout << ((float)i / 500) << '\n';
        zoom_wall(test_mtr, (float)i/500);
        setCursorPosition(0, 0);
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
