#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>

using namespace std;
typedef unsigned long long ull;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int n;
    cin >> n;

    if (n == 1) {
        cout << "*";
        return 0;
    }

    for (int i = 0; i < n - 1; ++i) {
        cout << " ";
    }
    cout << "*\n";

    for (int i = 0; i < n - 2; ++i) {
        for (int j = n - 2 - i; j > 0; --j) {
            cout << " ";
        }
        cout << "*";
        for (int j = 0; j < 2 * i + 1; ++j) {
            cout << " ";
        }
        cout << "*\n";
    }

    for (int i = 0; i < 2 * n - 1; ++i) {
        cout << "*";
    }
}
