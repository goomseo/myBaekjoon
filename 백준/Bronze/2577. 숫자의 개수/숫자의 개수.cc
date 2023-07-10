#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int n, result = 1;
    for (int i = 0; i < 3; ++i) {
        cin >> n;
        result *= n;
    }

    string tmp = to_string(result);
    int arr[10] = {0};
    for (int i = 0; i < tmp.length(); ++i)
        arr[tmp[i] - 48] += 1;

    for (int i = 0; i < 10; ++i)
        cout << arr[i] << '\n';
}
