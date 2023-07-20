#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<int> vec;
    for (int i = 0; i < n; ++i)
        vec.push_back(i + 1);

    int idx1, idx2;
    for (int i = 0; i < m; ++i) {
        cin >> idx1 >> idx2;

        if (idx1 != idx2)
            reverse(vec.begin() + idx1 - 1, vec.begin() + idx2);
    }

    for (int i : vec)
        cout << i << ' ';
}
