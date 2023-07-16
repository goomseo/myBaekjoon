#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int arr[201] = {0};

    int n, tmp;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> tmp;
        arr[tmp + 100] += 1;
    }

    int v;
    cin >> v;
    cout << arr[v + 100];
}
