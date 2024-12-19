#include <stdio.h>

void CalculateSquare(int num) {
    int square = num * num;
    printf("Square of %d is %d\n", num, square);
}

int main() {
    CalculateSquare(5);

    return 0;
}
