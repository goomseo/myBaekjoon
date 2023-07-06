#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int max = 0;
    int passengers = 0;
    int out, in;
    for (int i = 0; i < 4; ++i) {
        cin >> out >> in;
        passengers -= out;
        if (passengers > max)
            max = passengers;
        passengers += in;
        if (passengers > max)
            max = passengers;
    }

    cout << max;
}
