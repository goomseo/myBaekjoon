#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int n;
    cin >> n;
    cin.ignore();

    string s;
    for (int i = 0; i < n; ++i) {
        getline(cin, s);
        s[0] = toupper(s[0]);
        cout << s << '\n';
    }
}
