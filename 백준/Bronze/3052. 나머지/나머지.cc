#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int arr[42] = {0};
    int n;
    for (int i = 0; i < 10; ++i) {
        cin >> n;
        arr[n % 42] += 1;
    }

    int count = 0;
    for (int i : arr)
        if (i)
            count += 1;

    cout << count;
}
