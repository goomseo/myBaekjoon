#include <iostream>
#include <bitset>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int t;
    cin >> t;

    int n;
    for (int i = 0; i < t; ++i) {
        cin >> n;
        string bin = bitset<32>(n).to_string();
        reverse(bin.begin(), bin.end());

        for (int j = 0; j < bin.length(); ++j)
            if (bin[j] == '1')
                cout << j << ' ';
        cout << '\n';
    }
}
