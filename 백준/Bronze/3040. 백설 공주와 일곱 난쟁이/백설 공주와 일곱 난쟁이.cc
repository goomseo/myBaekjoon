#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    vector<int> vec;
    int tmp;
    for (int i = 0; i < 9; ++i) {
        cin >> tmp;
        vec.push_back(tmp);
    }

    int sum = accumulate(vec.begin(), vec.end(), 0);
    int a, b;
    for (int i = 0; i < 8; ++i) {
        for (int j = i + 1; j < 9; ++j) {
            if (sum - vec[i] - vec[j] == 100)
                a = vec[i], b = vec[j];
        }
    }

    for (int i = 0; i < 9; ++i) {
        if (vec[i] != a and vec[i] != b)
            cout << vec[i] << '\n';
    }
}
