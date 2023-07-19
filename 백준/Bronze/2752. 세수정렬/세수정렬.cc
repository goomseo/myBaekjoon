#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    vector<int> vec;
    int n;
    for (int i = 0; i < 3; ++i) {
        cin >> n;
        vec.push_back(n);
    }

    sort(vec.begin(), vec.end());

    cout << vec[0] << ' ' << vec[1] << ' ' << vec[2];
}
