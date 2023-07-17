#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int t;
    cin >> t;

    int n, tmp;
    vector<int> vec;
    for (int i = 0; i < t; ++i) {
        cin >> n;
        for (int j = 0; j < n; ++j) {
            cin >> tmp;
            vec.push_back(tmp);
        }
        
        sort(vec.begin(), vec.end());

        cout << (*(vec.end() - 1) - *vec.begin()) * 2 << '\n';
        
        vec.clear();
    }
}
