#include <stdio.h>

int main() {
    int tk;
    scanf("%d", &tk);

    if (tk >= 5000) {              // 1st condition
        printf("Cox's Bazar jabo\n");

        if (tk >= 10000) {         // nested if
            printf("Saint Martin jabo\n");
        }
        else {
            printf("ferot chole jabo\n");
        }
    }
    else {
        printf("kothayo jabo na\n");
    }

    return 0;
}
