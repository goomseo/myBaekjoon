#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int t;
    cin >> t;

    string a, b;
    for (int i = 0; i < t; ++i) {
        cin >> a >> b;

        int distance;
        vector<int> vec;
        for (int j = 0; j < a.length(); ++j) {
            distance = (a[j] <= b[j]) ? b[j] - a[j] : b[j] - a[j] + 26;
            vec.push_back(distance);
        }

        cout << "Distances: ";
        for (int j : vec)
            cout << j << ' ';
        cout << '\n';
    }
}
