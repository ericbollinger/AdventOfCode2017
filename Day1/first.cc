#include <fstream>
#include <iostream>
#include <stdio.h>

int main(int argc, char **argv) {
    char cur, prev, first;
    int sum = 0;

    std::fstream fin("input.txt", std::fstream::in);

    fin >> first;
    prev = first;

    while (fin >> cur) {
        if (cur == prev) {
            sum += (int) cur - 48;
        }
        prev = cur;
    }

    if (cur == first) {
        sum += (int) cur - 48;
    }
    
    std::cout << "Sum: " << sum << "\n";
}
