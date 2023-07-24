#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int k;
    cin >> k;

    int money;
    vector<int> vec;
    for (int i = 0; i < k; ++i) {
        cin >> money;

        if (money)
            vec.push_back(money);
        else
            vec.erase(vec.end() - 1);
    }

    cout << accumulate(vec.begin(), vec.end(), 0) << '\n';
}
