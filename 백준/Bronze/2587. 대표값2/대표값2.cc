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
    for (int i = 0; i < 5; ++i) {
        cin >> n;
        vec.push_back(n);
    }

    sort(vec.begin(), vec.end());
    cout << accumulate(vec.begin(), vec.end(), 0) / vec.size() << '\n' << vec[2];
}
