#include <iostream>

using namespace std;

int getPrice();

int main(){
    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
        cout << getPrice() << endl;

    return 0;
}

int getPrice(){
    int s;
    cin >> s;

    int n, q, p;
    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> q >> p;
        s += q * p;
    }

    return s;
}