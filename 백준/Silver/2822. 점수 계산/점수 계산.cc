#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    vector<int> vec;
    int n;
    for (int i = 0; i < 8; ++i) {
        cin >> n;
        vec.push_back(n);
    }

    vector<int> vec_copied(vec.size());
    copy(vec.begin(), vec.end(), vec_copied.begin());
    sort(vec_copied.begin(), vec_copied.end());

    int sum = 0;
    sum += *(vec_copied.end() - 1) + *(vec_copied.end() - 2) + *(vec_copied.end() - 3) + *(vec_copied.end() - 4) + *(vec_copied.end() - 5);

    cout << sum << '\n';

    vector<int> idx_vec;
    for (int i = 0; i < 5; ++i)
        idx_vec.push_back(find(vec.begin(), vec.end(), *(vec_copied.end() - i - 1)) - vec.begin() + 1);

    sort(idx_vec.begin(), idx_vec.end());
    for (int i : idx_vec)
        cout << i << ' ';
}
