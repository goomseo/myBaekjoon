#include <stdio.h>
#include <stdlib.h>

int static compare(const void* first, const void* second)
{
    if (*(int *) first > *(int *) second)
        return 1;
    else if (*(int *) first < *(int *) second)
        return -1;
    else
        return 0;
}

int main(void)
{
    int n;
    scanf("%d", &n);

    int arr[51] = {0};
    for (int i = 0; i < n; i++)
        scanf(" %d", &arr[i]);

    qsort(arr, n, sizeof(int), compare);

    printf("%d", arr[0] * arr[n - 1]);

    return 0;
}