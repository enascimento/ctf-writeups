#include <stdio.h>

int main() {
    float number = 0.25;
    long i;
    float x2, y;
    const float threehalfs = 1.5F;
 
    x2 = number * 0.5F;
    y  = number;
    i  = * ( long * ) &y;                       // evil floating point bit level hacking
    i  = 0x5f3759df - ( i >> 1 );               // what the fuck?
    y  = * ( float * ) &i;

    for (int i = 0; i < 5; i++) {
        printf("Flag calculating... %f\n", y);
        y  = y * ( threehalfs - ( x2 * y * y ) );
    }
}