#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>

using namespace std;
typedef unsigned long long ull;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int arr[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    int x, y;
    cin >> x >> y;

    int days = 0;
    for (int i = 0; i < x - 1; ++i)
        days += arr[i];
    days += y;

    string week[7] = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
    cout << week[days % 7];
}
