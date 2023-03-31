#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    int holes;
    int sum = 0;
    for (int i = 0; i < n; i++){
        cin >> holes;
        sum += holes;
    }

    cout << sum - n + 1;

    return 0;
}
