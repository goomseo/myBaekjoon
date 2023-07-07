#include <iostream>

using namespace std;

int getReversed(int n) {
    int result = 0;

    while (true) {
        if (n == 0)
            break;

        result += n % 10;
        result *= 10;
        n /= 10;
    }

    return result / 10;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int a, b;
    cin >> a >> b;

    a = getReversed(a);
    b = getReversed(b);

    cout << ((a > b) ? a : b);
}
