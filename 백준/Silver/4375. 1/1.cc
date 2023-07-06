#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    while (true) {
        int n;
        cin >> n;

        if (cin.eof())
            break;

        int obj = 1, digits = 1;
        while (true) {
            if (obj % n == 0)
                break;

            obj = obj * 10 + 1;
            obj %= n;
            digits += 1;
        }

        cout << digits << '\n';
    }
}
