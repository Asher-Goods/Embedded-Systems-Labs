#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>
#include <signal.h>
#include <unistd.h>
#include <signal.h>

// Define a custom signal handler function
void custom_signal_handler(int signum) {
    if (signum == SIGALRM) {
        printf("Timer expired - Interrupt received!\n");
        // Perform any desired actions here
    }
}

int main() {
    struct itimerval timer;
    struct sigaction sa;

    // Initialize the custom signal handler
    memset(&sa, 0, sizeof(sa));
    sa.sa_handler = &custom_signal_handler;
    sigaction(SIGALRM, &sa, NULL);

    // Configure the timer
    timer.it_value.tv_sec = 10;  // Initial timer value in seconds
    timer.it_value.tv_usec = 0; // Initial timer value in microseconds
    timer.it_interval.tv_sec = 0;  // Timer interval (0 means one-shot timer)
    timer.it_interval.tv_usec = 0;

    // Set the timer using setitimer
    if (setitimer(ITIMER_REAL, &timer, NULL) == -1) {
        perror("setitimer");
        exit(1);
    }

    // Wait for the interrupt to occur (infinite loop)
    while (1) {
        sleep(1);
    }

    return 0;
}