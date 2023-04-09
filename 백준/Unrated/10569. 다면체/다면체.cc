#include <iostream>

using namespace std;

int main(){
    int t;
    cin >> t;

    int v, e;
    for (int i = 0; i < t; i++){
        cin >> v >> e;
        cout << 2 - v + e << endl;
    }

    return 0;
}