#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
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
