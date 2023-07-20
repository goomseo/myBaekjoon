#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<int> vec(n, 0);
    int start, end, num;
    for (int i = 0; i < m; ++i) {
        cin >> start >> end >> num;
        for (int j = start; j < end + 1; ++j)
            vec[j - 1] = num;
    }

    for (int i : vec)
        cout << i << ' ';
}
