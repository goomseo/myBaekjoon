#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>

using namespace std;
typedef unsigned long long ull;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    string s;
    cin >> s;

    vector<string> vec;
    while (s.length() != 0) {
        vec.push_back(s);
        s.erase(s.begin(), s.begin() + 1);
    }

    sort(vec.begin(), vec.end());
    for (const string& str : vec)
        cout << str << '\n';
}
