#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int n;
    cin >> n;

    unsigned long long factorial = 1;
    for (int i = 0; i < n; ++i) {
        factorial *= i + 1;
    }

    cout << factorial;
}
