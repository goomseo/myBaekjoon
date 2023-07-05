#include <iostream>
#include <cmath>
#include <vector>
#include <numeric>

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

    vector<int> vec;
    for (int i = m; i < n + 1; ++i) {
        if (isPrime(i))
            vec.push_back(i);
    }

    if (vec.size()) {
        cout << accumulate(vec.begin(), vec.end(), 0) << '\n';
        cout << vec[0];
    }
    else
        cout << -1;
}
