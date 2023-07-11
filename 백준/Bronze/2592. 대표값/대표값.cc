#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int arr[99] = {0}, n;
    for (int i = 0; i < 10; ++i) {
        cin >> n;
        arr[n / 10 - 1] += 1;
    }

    int sum = 0, mode, tmp = 0;
    for (int i = 0; i < 99; ++i) {
        sum += arr[i] * (10 * (i + 1));

        if (arr[i] >= tmp) {
            tmp = arr[i];
            mode = 10 * (i + 1);
        }
    }

    cout << sum / 10 << '\n' << mode;
}
