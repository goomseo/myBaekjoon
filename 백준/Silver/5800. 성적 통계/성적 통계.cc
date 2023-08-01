#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int k;
    cin >> k;

    int n;
    for (int i = 0; i < k; ++i) {
        cin >> n;
        vector<int> vec(n);
        for (int j = 0; j < n; ++j)
            cin >> vec[j];

        cout << "Class " << i + 1 << '\n';
        cout << "Max " << *max_element(vec.begin(), vec.end()) << ", Min " << *min_element(vec.begin(), vec.end());

        sort(vec.begin(), vec.end());
        int max_gap = 0;
        for (int j = 0; j < n - 1; ++j)
            if (vec[j+1] - vec[j] >= max_gap)
                max_gap = vec[j+1] - vec[j];
        cout << ", Largest gap " << max_gap << '\n';
    }
}
