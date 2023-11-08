#include <stdio.h>

int main() {
    int periodA, periodB;
    int execTimeA, execTimeB;
    int absDeadlineA, absDeadlineB;
    float cpuUtil;
    int jA = -1, jB = -1;
    int doA = 0, doB = 0;
    int tA = 0, tB = 0;
    int T;

    printf("\t\t\t---------------------------------------\n");
    printf("\t\t\tEarliest Deadline First (EDF) Algorithm\n");
    printf("\t\t\t---------------------------------------\n");
    printf("Please input period and execution for A process\ndefault: 25, 10: ");
    scanf("%d%d", &periodA, &execTimeA);
    printf("Please input period and execution for B process\ndefault: 60, 15: ");
    scanf("%d%d", &periodB, &execTimeB);

    cpuUtil = ((double)(execTimeA) / (double)(periodA) + (double)(execTimeB) / (double)(periodB));
    printf("CPU Utilization: %.2f\n", cpuUtil);

    absDeadlineA = periodA;
    absDeadlineB = periodB;
    printf("\nSimulation started\n");

    for (T = 0; T <= 200; T++) {
        if (doA && T > absDeadlineA) {
            printf("Process A missed deadline! Not schedulable\n");
            break;
        } else if (doB && T > absDeadlineB) {
            printf("Process B missed deadline! Not schedulable\n");
            break;
        }

        if (tA == execTimeA && doA == 1) {
            printf("when T=%d, process A%d is done\n", T, jA);
            doA = 0;
            if (tB < execTimeB) {
                printf("when T=%d, program switched to run process B%d!\n", T, jB);
                doB = 1;
            }
        }

        if (tB == execTimeB && doB == 1) {
            printf("when T=%d, process B%d is done\n", T, jB);
            doB = 0;
            if (tA < execTimeA) {
                printf("when T=%d, program switched to run process A%d!\n", T, jA);
                doA = 1;
            }
        }

        if (T % periodA == 0 && T % periodB == 0) {
            printf("when T=%d, process A%d and B%d are generated together\n", T, ++jA, ++jB);
            absDeadlineA = T + periodA;
            absDeadlineB = T + periodB;
            if (absDeadlineA < absDeadlineB) {
                printf("when T=%d, program switched to run process A%d!\n", T, jA);
                doA = 1;
                doB = 0;
            } else {
                printf("when T=%d, program switched to run process B%d!\n", T, jB);
                doA = 0;
                doB = 1;
            }
            tA = 0;
            tB = 0;
        }

        if (T % periodA == 0 && T % periodB != 0) {
            printf("when T=%d, process A%d is generated\n", T, ++jA);
            absDeadlineA = T + periodA;
            tA = 0;
            if (tB < execTimeB && execTimeB - tB > execTimeA) {
                printf("when T=%d, program switched to run process B%d!\n", T, jB);
                doA = 0;
                doB = 1;
            }
            else{
                printf("when T=%d, program switched to run process A%d!\n", T, jA);
                doA = 1;
                doB = 0;
            }
        }

        if (T % periodA != 0 && T % periodB == 0) {
            printf("when T=%d, process B%d is generated\n", T, ++jB);
            absDeadlineB = T + periodB;
            tB = 0;
            if (tA < execTimeA && execTimeA - tA > execTimeB) {
                printf("when T=%d, program switched to run process A%d!\n", T, jA);
                doA = 1;
                doB = 0;
            }
            else{
                printf("when T=%d, program switched to run process B%d!\n", T, jB);
                doA = 0;
                doB = 1;
            }
        }

        if (doA) {
            tA++;
        }
        if (doB) {
            tB++;
        }
    }
}
