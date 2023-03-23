#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    long long a = 0, b = 1;
    long long tmp;
    for (int i = 0; i < n; i++){
        tmp = b;
        b += a;
        a = tmp;
    }

    cout << a << endl;

    return 0;
}
