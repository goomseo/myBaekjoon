#include <iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int n;
    cin >> n;

    int c, v;
    for (int i = 0; i < n; ++i){
        cin >> c >> v;
        cout << "You get " << c / v << " piece(s) and your dad gets " << c % v << " piece(s).\n";
    }
}