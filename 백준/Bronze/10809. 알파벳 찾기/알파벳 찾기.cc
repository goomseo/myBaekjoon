#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    vector<int> vec(26, -1);
    string s;
    cin >> s;

    for (char c : s)
        vec[c - 'a'] = s.find(c);

    for (int i : vec)
        cout << i << ' ';
}
