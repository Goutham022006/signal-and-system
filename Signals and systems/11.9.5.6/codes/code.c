#include <stdio.h>

int calculate_y(int n) {
    return (n + 1) * (13 + 2 * n);
}

int main() {
    FILE *outputFile;
    int n;

    // Open a file for writing
    outputFile = fopen("output.txt", "w");

    if (outputFile == NULL) {
        printf("Error opening the file.\n");
        return 1;
    }

    // Calculate and write values to the file
    for (n = 0; n <= 10; ++n) {
        int result = calculate_y(n);
        fprintf(outputFile, "%d %d\n", n, result);
    }

    // Close the file
    fclose(outputFile);

    return 0;
}

