#include <iostream>
using namespace std;

bool isPerfectSquare(int x);

int main()
{
    int m, n, min;
    int sum = 0;
    cin >> m >> n;

    for (int i = m; i < (n + 1); i++)
    {
        if (isPerfectSquare(i))
        {
            sum += i;

            if (sum == i)
                min = i;
        }
    }

    if (sum == 0)
        cout << -1 << endl;
    else
    {
        cout << sum << endl;
        cout << min << endl;
    }

    return 0;
}

bool isPerfectSquare(int x)
{
    for (int i = 1; i <= x; i++)
        if (i * i == x)
            return true;

    return false;
}