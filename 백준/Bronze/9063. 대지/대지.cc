#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int n;
    cin >> n;

    int arr_x[n], arr_y[n];
    for (int i = 0; i < n; ++i)
        cin >> arr_x[i] >> arr_y[i];

    sort(arr_x, arr_x + n);
    sort(arr_y, arr_y + n);

    cout << (arr_x[n - 1] - arr_x[0]) * (arr_y[n - 1] - arr_y[0]);
}
