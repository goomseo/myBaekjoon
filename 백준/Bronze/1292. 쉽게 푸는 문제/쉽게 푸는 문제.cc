#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    vector<int> vec;
    for (int i = 0; i < 1000; ++i)
        for (int j = 0; j < i + 1; ++j)
            vec.push_back(i + 1);

    int start, end;
    cin >> start >> end;

    int sum = 0;
    for (int i = start - 1; i < end; ++i)
        sum += vec[i];

    cout << sum;
}
