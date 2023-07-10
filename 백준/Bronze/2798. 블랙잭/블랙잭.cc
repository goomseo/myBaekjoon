#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int n, m;
    cin >> n >> m;

    int arr[n];
    for (int i = 0; i < n; ++i)
        cin >> arr[i];

    int max = 0, sum;
    for (int i = 0; i < n - 2; ++i) {
        for (int j = i + 1; j < n - 1; ++j) {
            for (int k = j + 1; k < n; ++k) {
                sum = arr[i] + arr[j] + arr[k];
                if (sum <= m and sum >= max)
                    max = sum;
            }
        }
    }

    cout << max;
}
