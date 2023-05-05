#include <iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int n;
    cin >> n;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < i; ++j)
            cout << " ";
        for (int j = 2 * (n - i - 1) + 1; j > 0; --j)
            cout << "*";
        cout << '\n';
    }
}