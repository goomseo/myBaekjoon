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
    int score;
    for (int i = 0; i < t; ++i) {
        for (int j = 0; j < 5; ++j) {
            cin >> score;
            vec.push_back(score);
        }

        sort(vec.begin(), vec.end());

        if (*(vec.end() - 2) - *(vec.begin() + 1) < 4)
            cout << accumulate(vec.begin() + 1, vec.end() - 1, 0) << '\n';
        else
            cout << "KIN\n";

        vec.clear();
    }
}
