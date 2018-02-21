#include <stdio.h>

int rabbit_hole(int arg0) {
    int eax = 1;
    if (arg0 > 0) {
        eax = rabbit_hole(arg0 - 4) + rabbit_hole(arg0 - 2);
    }
    return eax;
}

int main() {
    for (int i = 0; i < 1024; i++) {
        printf("\rCurrently on %d", i);
        fflush(stdout);
        if (rabbit_hole(i >> 0x3) == 0x3c50ea2) {
            printf("\nFound! %d\n", i);
            return 0;
        }
    }
    return 1;
}
