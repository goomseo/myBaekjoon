#include <stdio.h>

int main(void)
{
    int a, b;
    scanf("%d %d", &a, &b);

    printf("%.50lf\n",  (double) a / b);

    return 0;
}