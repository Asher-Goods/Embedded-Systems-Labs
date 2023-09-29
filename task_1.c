#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#define N 1024

float A[N][N];
float B[N][N];
float C[N][N];

// Function to multiply two matrices A and B of size N
void multiplyMatrices(float A[][N], float B[][N], float C[][N])
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            C[i][j] = 0; // Initialize the result matrix element to 0
            for (int k = 0; k < N; k++)
            {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

int main()
{

    /* Randomly initialize the matrices */
    srand((unsigned)time(NULL));
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            A[i][j] = rand() / (float)RAND_MAX;
            B[i][j] = rand() / (float)RAND_MAX;
        }
    }

    /*timer setup*/
    clock_t start_time = clock();

    /* Code for matrix multiplication    C <- A x B*/
    multiplyMatrices(A, B, C);

    clock_t end_time = clock();
    float elapse = (float)(end_time - start_time) / CLOCKS_PER_SEC;
    
    printf("elapse: %.4f seconds\n", elapse);

    return 0;
}
