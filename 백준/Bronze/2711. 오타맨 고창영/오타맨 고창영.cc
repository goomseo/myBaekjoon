#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int t;
    cin >> t;

    int idx;
    string str;
    for (int i = 0; i < t; ++i) {
        cin >> idx >> str;

        str.erase(idx - 1, 1);
        cout << str << '\n';
    }
}
