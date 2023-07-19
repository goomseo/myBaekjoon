#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    vector<int> hamburgers;
    int a, b, c;
    cin >> a >> b >> c;
    hamburgers.push_back(a);
    hamburgers.push_back(b);
    hamburgers.push_back(c);

    vector<int> beverages;
    int d, e;
    cin >> d >> e;
    beverages.push_back(d);
    beverages.push_back(e);

    cout << *min_element(hamburgers.begin(), hamburgers.end()) + *min_element(beverages.begin(), beverages.end()) - 50;
}
