#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#define N 1024;

float A[N][N];
float B[N][N];
float C[N][N];

int main()
{

    /* Randomly initialize the matrices */
    srand((unsigned)time(NULL));
    for(int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            A[i][j] = rand()/(float)RAND_MAX;
            B[i][j] = rand()/(float)RAND_MAX;
        }
    }

    /*timer setup*/
    clock_t start_time = clock();

    /* Code for matrix multiplication    C <- A x B*/ 


    clock_t end_time = clock();
    float elapse = (float)(end_time - start_time) / CLOCKS_PER_SEC;
    printf("elapse: %.4f seconds\n", elapse);

    return 0;

}

