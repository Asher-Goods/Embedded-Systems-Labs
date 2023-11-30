#include <stdio.h>
#include <stdlib.h>

int main(){
    int result = 0; const long int repeating_time = 500000000;

    for (long int i = 0; i < repeating_time; i++){
        if (result > 1000) {result -=1;} else {result +=1;}
    }
}