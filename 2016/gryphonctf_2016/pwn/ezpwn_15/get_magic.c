#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    srand(time(NULL));

    int j = rand() % 12345678 * -1;
    int r = j + 0;

    printf("%d", r);
    return 0;
}