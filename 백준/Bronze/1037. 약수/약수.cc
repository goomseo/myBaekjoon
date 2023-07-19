#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    vector<int> vec;
    int t;
    cin >> t;

    int tmp;
    for (int i = 0; i < t; ++i) {
        cin >> tmp;
        vec.push_back(tmp);
    }

    sort(vec.begin(), vec.end());

    cout << *vec.begin() * *(vec.end() - 1);
}
