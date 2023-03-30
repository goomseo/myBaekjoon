#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int a, b;
    cin >> a >> b;

    if (a > b){
        a = a ^ b;
        b = a ^ b;
        a = a ^ b;
    }

    for (int i = a + 1; i > 0; i--)
        if ((a % i == 0) and (b % i == 0)){
            cout << i << endl;
            break;
        }

    int j = 1;
    while (true){
        if ((b * j) % a == 0){
            cout << b * j << endl;
            break;
        }

        j++;
    }

    return 0;
}
