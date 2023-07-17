#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int n;
    cin >> n;

    int tmp;
    vector<int> vec;
    for (int i = 0; i < n; ++i) {
        cin >> tmp;
        vec.push_back(tmp);
    }
    
    sort(vec.begin(), vec.end());
    for (int i : vec)
        cout << i << '\n';
}
