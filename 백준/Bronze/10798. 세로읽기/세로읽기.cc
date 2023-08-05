#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    vector<vector<string>> vec(5, vector<string>(15, " "));
    string s;
    for (auto & i : vec) {
        cin >> s;
        for (int j = 0; j < s.length(); ++j)
            i[j] = s[j];
    }

    for (int i = 0; i < 15; ++i)
        for (auto & j : vec)
            if (j[i] != " ")
                cout << j[i];
}
