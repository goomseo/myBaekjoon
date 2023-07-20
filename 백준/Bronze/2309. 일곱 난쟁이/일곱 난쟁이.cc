#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    vector<int> vec;
    int n;
    for (int i = 0; i < 9; ++i) {
        cin >> n;
        vec.push_back(n);
    }

    int sum = accumulate(vec.begin(), vec.end(), 0);
    int a, b;
    for (int i = 0; i < vec.size() - 1; ++i) {
        for (int j = i + 1; j < vec.size(); ++j) {
            if (sum - vec[i] - vec[j] == 100) {
                a = vec[i];
                b = vec[j];
            }
        }
    }

    sort(vec.begin(), vec.end());
    for (int i : vec)
        if (not((i == a) or (i == b)))
            cout << i << '\n';
}
