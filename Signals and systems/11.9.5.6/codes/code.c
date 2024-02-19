#include <stdio.h>

int main() {
    FILE *fp;
    fp = fopen("ap_sum_data.txt", "w"); // Open file for writing

    if (fp == NULL) {
        printf("Error opening file!");
        return 1;
    }

    int start = 13; // Starting term
    int diff = 4;   // Common difference
    int n = 22;     // Number of terms, including the 22nd term to be highlighted
    int sum = 0;

    printf("Sum of Arithmetic Progression:\n");
    for (int i = 1; i <= n; i++) {
        int term = start + (i - 1) * diff;
        sum += term;
        printf("%d\n", sum);
        fprintf(fp, "%d\n", sum); // Write sum to file
    }

    fclose(fp); // Close the file
    return 0;
}

