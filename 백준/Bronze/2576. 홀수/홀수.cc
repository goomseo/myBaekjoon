#include <iostream>

using namespace std;

int main(){
    int min = 100, sum = 0, num;
    for (int i = 0; i < 7; i++){
        cin >> num;

        if (num % 2){
            sum += num;

            if (num < min)
                min = num;
        }
    }

    if (!sum)
        cout << -1 << endl;
    else
        cout << sum << endl << min << endl;

    return 0;
}