# C
```C
#include "stdio.h"

int main() {
    printf("Hello, World!");
    return 0;
}
```
## Memory pointers and dereferencing
```C
#include <stdio.h>
#include <string.h>

void println(char *s) {
    printf(s, "");
    printf("\n");
}

int main() {
    char *test = "Hello World!";
    char **tested = &test; //Declaring tested as a pointer to test
    println(*tested); //passes the value of the referenced pointer at `tested` to println()
    return 0;
}
```
