#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    vector<int> vec;
    int a, b, c, d, e;
    cin >> a >> b >> c >> d >> e;
    vec.push_back(a);
    vec.push_back(b);
    vec.push_back(c);
    vec.push_back(d);
    vec.push_back(e);

    sort(vec.begin(), vec.end());
    cout << accumulate(vec.begin(), vec.end(), 0) / vec.size() << '\n' << vec[2];
}
