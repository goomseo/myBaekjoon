#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int arr[3];
    cin >> arr[0] >> arr[1] >> arr[2];

    sort(arr, arr + 3);

    while (true) {
        if (arr[2] >= arr[0] + arr[1])
            arr[2] -= 1;
        else
            break;
    }

    cout << arr[0] + arr[1] + arr[2];
}
