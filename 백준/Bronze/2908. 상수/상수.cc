#include <iostream>
#include <algorithm>

using namespace std;

int getReversed(int n) {
    string result = to_string(n);
    reverse(result.begin(), result.end());

    return stoi(result);
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
