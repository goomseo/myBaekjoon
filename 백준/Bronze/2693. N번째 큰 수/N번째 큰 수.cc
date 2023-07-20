#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int t;
    cin >> t;

    vector<int> vec;
    int n;
    for (int i = 0; i < t; ++i) {
        for (int j = 0; j < 10; ++j) {
            cin >> n;
            vec.push_back(n);
        }

        sort(vec.begin(), vec.end());

        cout << vec[7] << '\n';

        vec.clear();
    }
}
