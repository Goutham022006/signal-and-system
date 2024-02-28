#include <stdio.h>
#include <math.h>

double calculate_X(double s) {
    if (s == 0) return 1.0;  // Avoid division by zero

    return 2*exp(-s) / (s * s * s);
}

int main() {
     FILE *fp = fopen("output.txt", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    // Calculate and write values to file
    for (int s = 0; s <= 8; s++) {
        double result = calculate_X(s);
        fprintf(fp, "%.10f\n", result);  // Write with high precision
    }

    fclose(fp);
    printf("Output values have been written to output.txt\n");
    return 0;
}

