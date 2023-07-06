#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int t;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        int n;
        cin >> n;

        int sum = 0, x;
        for (int j = 0; j < n; ++j) {
            cin >> x;
            sum += x;
        }

        cout << sum << '\n';
    }
}
