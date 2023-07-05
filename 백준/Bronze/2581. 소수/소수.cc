#include <iostream>
#include <cmath>

using namespace std;

bool isPrime(int n) {
    if (n == 1)
        return false;

    for (int i = 2; i < int(sqrt(n)) + 1; ++i)
        if (n % i == 0)
            return false;

    return true;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int m, n;
    cin >> m;
    cin >> n;

    int sum = 0, min = n, count = 0;
    for (int i = m; i < n + 1; ++i) {
        if (isPrime(i)) {
            sum += i;
            if (i < min)
                min = i;
            count += 1;
        }
    }

    if (count) {
        cout << sum << '\n';
        cout << min;
    }
    else
        cout << -1;
}
