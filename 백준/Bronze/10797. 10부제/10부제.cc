#include <iostream>

using namespace std;

int main(){
    int date;
    cin >> date;
    
    int arr[5], sum = 0;
    for (int i = 0; i < 5; i++){
        cin >> arr[i];
        
        if (date == arr[i])
            sum += 1;
    }
    
    cout << sum << endl;

    return 0;
}