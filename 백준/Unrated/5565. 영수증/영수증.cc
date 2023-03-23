#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int total;
    cin >> total;

    int bookPrice;
    for (int i = 0; i < 9; i++){
        cin >> bookPrice;
        total -= bookPrice;
    }

    cout << total << endl;

    return 0;
}
