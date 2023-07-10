#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int arr[3];
    while (true) {
        cin >> arr[0] >> arr[1] >> arr[2];
        if (arr[0] + arr[1] + arr[2] == 0)
            break;

        sort(arr, arr + 3);

        if (arr[2] >= arr[0] + arr[1])
            cout << "Invalid\n";
        else if ((arr[0] == arr[1]) and (arr[0] == arr[2]))
            cout << "Equilateral\n";
        else if ((arr[0] != arr[1]) and (arr[0] != arr[2]) and (arr[1] != arr[2]))
            cout << "Scalene\n";
        else
            cout << "Isosceles\n";
    }
}
