#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int k;
    cin >> k;

    int p, m;
    for (int i = 0; i < k; ++i) {
        cin >> p >> m;

        vector<int> vec(p, 0);
        int tmp, count = 0;
        for (int j = 0; j < p; ++j) {
            cin >> tmp;

            if (vec[tmp - 1] == 0)
                vec[tmp - 1] += 1;
            else
                count += 1;
        }

        cout << count << '\n';
    }
}
