#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int n, m;
    cin >> n >> m;

    string s = to_string(n), result;
    for (int i = 0; i < n; ++i)
        result += s;

    if (result.length() <= m)
        cout << result;
    else
        for (int i = 0; i < m; ++i)
            cout << result[i];
}
