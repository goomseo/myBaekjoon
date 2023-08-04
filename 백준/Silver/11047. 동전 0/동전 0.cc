#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int n, k;
    cin >> n >> k;

    vector<int> vec(n);
    for (int i = 0; i < n; ++i) {
        cin >> vec[i];
    }

    reverse(vec.begin(), vec.end());

    int count = 0;
    for (int coin : vec) {
        while (k >= coin) {
            k -= coin;
            count += 1;
        }
    }

    cout << count;
}
