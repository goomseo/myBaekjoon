#include <iostream>
#include <vector>

using namespace std;

void swap(int &a, int &b) {
    a = a ^ b;
    b = a ^ b;
    a = a ^ b;
}

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
            swap(vec[idx1 - 1], vec[idx2 - 1]);
    }

    for (int i : vec)
        cout << i << ' ';
}
