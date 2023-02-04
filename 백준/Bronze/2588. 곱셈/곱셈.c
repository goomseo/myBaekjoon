#include <stdio.h>

int main(void)
{
    int a, b;
    scanf("%d", &a);
    scanf("%d", &b);

    int first, second, third;
    int answer;

    first = a * (b % 10);
    b /= 10;
    second = a * (b % 10);
    b /= 10;
    third = a * (b % 10);

    answer = first + second * 10 + third * 100;

    printf("%d\n%d\n%d\n%d\n", first, second, third, answer);

    return 0;
}