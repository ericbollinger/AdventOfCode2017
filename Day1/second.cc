#include <fstream>
#include <iostream>
#include <stdio.h>

int main(int argc, char **argv) {
    // Get length of input file
    FILE *p_file = NULL;
    p_file = fopen("input.txt", "rb");
    fseek(p_file, 0, SEEK_END);
    int length = ftell(p_file) - 1;
    fclose(p_file);

    // Load array with file contents
    char cur;
    int arr[length];

    std::fstream fin("input.txt", std::fstream::in);

    for (int i = 0; i < length; i++) {
        fin >> cur;
        arr[i] = (int) cur - 48;
    }

    // Compute
    int half = length/2;
    int sum = 0;

    for (int i = 0; i < length; i++) {
        if (arr[i] == arr[(i + half) % length]) {
            sum += arr[i];
        }
    }

    std::cout << "Sum: " << sum << "\n";
    
}
