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
    int tmp;
    for (int i = 0; i < t; ++i) {
        for (int j = 0; j < 7; ++j) {
            cin >> tmp;

            if (tmp % 2 == 0)
                vec.push_back(tmp);
        }

        cout << accumulate(vec.begin(), vec.end(), 0) << ' ' << *min_element(vec.begin(), vec.end()) << '\n';
        
        vec.clear();
    }
}
