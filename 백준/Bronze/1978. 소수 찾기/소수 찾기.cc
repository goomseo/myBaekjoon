#include <iostream>

using namespace std;

bool isPrime(int n) {
    if (n == 1)
        return false;

    for (int i = 2; i < n; ++i) {
        if (n % i == 0)
            return false;
    }

    return true;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int n;
    cin >> n;

    int arr[n];
    int countPrime = 0;
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];

        if (isPrime(arr[i]))
            countPrime += 1;
    }

    cout << countPrime;
}
