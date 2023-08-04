#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    string s;
    getline(cin, s);

    for (char &c : s) {
        if (isalpha(c)) {
            if ((c <= 'm' and c >= 'a') or (c <= 'M' and c >= 'A'))
                c += 13;
            else
                c -= 13;
        }
    }

    cout << s;
}
