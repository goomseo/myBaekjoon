#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    for (int i = 0; i < 9; i++)
        cout << n << " * " << i + 1 << " = " << n * (i + 1) << endl;

    return 0;
}
