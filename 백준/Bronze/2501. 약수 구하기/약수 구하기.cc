#include <iostream>
#include <vector>

using namespace std;

bool isDivisor(int n, int i) {
    if (n % i)
        return false;

    return true;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int n, k;
    cin >> n >> k;

    vector<int> vec;
    for (int i = 1; i < n + 1; ++i) {
        if (isDivisor(n, i))
            vec.push_back(i);
    }

    if (vec.size() < k)
        cout << 0;
    else
        cout << vec[k - 1];
}
