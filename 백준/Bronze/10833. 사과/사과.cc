#include <iostream>
using namespace std;

int main()
{
    int sum = 0;
    int n;
    cin >> n;

    int a, b;
    for (int i = 0; i < n; ++i){
        cin >> a >> b;
        sum += b % a;
    }

    cout << sum;
}