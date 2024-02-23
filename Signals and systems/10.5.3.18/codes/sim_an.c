#include <stdio.h>

void convolution(const float *array1, int len1, const float *array2, int len2, float *result) {
    int lenResult = len1 + len2 - 1;
    for (int i = 0; i < lenResult; i++) {
        result[i] = 0;
    }
    for (int i = 0; i < len1; i++) {
        for (int j = 0; j < len2; j++) {
            result[i + j] += array1[i] * array2[j];
        }
    }
}

void sum_of_ap(float a, float d, int N) {

    float x[N];
    for (int i = 0; i < N; i++) {
        x[i] = a + i * d;
    }

    float u[N];
    for (int i = 0; i < N; i++) {
        u[i] = 1;
    }
 
    float result[N + N - 1];
    convolution(x, N, u, N, result);
    FILE *file = fopen("result_terms.txt", "w");
    if (file == NULL) {
        printf("Error opening file.\n");
    }
    for (int i = 0; i < N ; i++) {
        fprintf(file, "%f\n", result[i]);
    }
    fclose(file);
}

int main() {
    float a = 1.571428;  // First term of the arithmetic progression
    float d = 3.142857;  // Common difference of the arithmetic progression
    int N = 15; // Number of terms to sum

    // Computing the sum of the first N terms of the AP
    sum_of_ap(a, d, N);
    return 0;
}

