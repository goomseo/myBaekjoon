#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int score, sum = 0, max = 0, id;
    for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < 4; ++j) {
            cin >> score;
            sum += score;
        }

        if (sum >= max) {
            max = sum;
            id = i + 1;
        }

        sum = 0;
    }

    cout << id << ' ' << max;
}
